# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = '''
    callback: detailed
    type: stdout
    short_description: detailed stdout callback plugin 
    version_added: 2.7
    description:
        - Produces very detailed yet accessible output when running a playbooks
        Will add a final report with changes after the run
    extends_documentation_fragment:
      - default_callback
    requirements:
      - set as stdout in configuration
'''


import inspect
import yaml
import json
import re
import string

from ansible import constants as C
from ansible.playbook.task_include import TaskInclude
from ansible.plugins.callback.default import CallbackModule as Default
from ansible.utils.color import colorize, hostcolor
from ansible.module_utils._text import to_bytes, to_text
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.callback import CallbackBase, strip_internal_keys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GRAY = '\033[30m'
    UNDERLINE = '\033[4m'


# from http://stackoverflow.com/a/15423007/115478
def should_use_block(value):
    """Returns true if string should be in block format"""
    for c in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2028\u2029":
        if c in value:
            return True
    return False

def my_represent_scalar(self, tag, value, style=None):
    """Uses block style for multi-line strings"""
    if style is None:
        if should_use_block(value):
            style = '|'
            # we care more about readable than accuracy, so...
            # ...no trailing space
            value = value.rstrip()
            # ...and non-printable characters
            value = ''.join(x for x in value if x in string.printable)
            # ...tabs prevent blocks from expanding
            value = value.expandtabs()
            # ...and odd bits of whitespace
            value = re.sub(r'[\x0b\x0c\r]', '', value)
            # ...as does trailing space
            value = re.sub(r' +\n', '\n', value)
        else:
            style = self.default_style
    node = yaml.representer.ScalarNode(tag, value, style=style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    return node



class CallbackModule(Default):

    debug = False

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'default'

    report=[]

    def __init__(self):
        super(CallbackModule, self).__init__()
        yaml.representer.BaseRepresenter.represent_scalar = my_represent_scalar

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=False):
        if result.get('_ansible_no_log', False):
            return json.dumps(dict(censored="The output has been hidden due to the fact that 'no_log: true' was specified for this result"))

        # All result keys stating with _ansible_ are internal, so remove them from the result before we output anything.
        abridged_result = strip_internal_keys(result)

        # remove invocation unless specifically wanting it
        if not keep_invocation and self._display.verbosity < 3 and 'invocation' in result:
            del abridged_result['invocation']

        # remove diff information from screen output
        if self._display.verbosity < 3 and 'diff' in result:
            del abridged_result['diff']

        # remove exception from screen output
        if 'exception' in abridged_result:
            del abridged_result['exception']

        dumped = ''

        # put changed and skipped into a header line
        if 'changed' in abridged_result:
            dumped += 'changed=' + str(abridged_result['changed']).lower() + ' '
            del abridged_result['changed']

        if 'skipped' in abridged_result:
            dumped += 'skipped=' + str(abridged_result['skipped']).lower() + ' '
            del abridged_result['skipped']

        # if we already have stdout, we don't need stdout_lines
        if 'stdout' in abridged_result and 'stdout_lines' in abridged_result:
            abridged_result['stdout_lines'] = '<omitted>'

        # if we already have stderr, we don't need stderr_lines
        if 'stderr' in abridged_result and 'stderr_lines' in abridged_result:
            abridged_result['stderr_lines'] = '<omitted>'

        if abridged_result:
            dumped += '\n'
            dumped += to_text(yaml.dump(abridged_result, allow_unicode=True, width=1000, Dumper=AnsibleDumper, default_flow_style=False))

        # indent by a couple of spaces
        dumped = '\n  '.join(dumped.split('\n')).rstrip()
        return dumped

    def _serialize_diff(self, diff):
        return to_text(yaml.dump(diff, allow_unicode=True, width=1000, Dumper=AnsibleDumper, default_flow_style=False))



    def add_to_report(self,msg,t="msg",host="",task=""):
        self.report.append({"t":t,"data":msg,"host":host,"task":task})

    def crete_task_banner(self,task):

        args = ''
        if not task.no_log and C.DISPLAY_ARGS_TO_STDOUT:
            args = u', '.join(u'%s=%s' % a for a in task.args.items())
            args = u' %s' % args

        prefix = self._task_type_cache.get(task._uuid, 'TASK')

        # Use cached task name
        task_name = self._last_task_name
        if task_name is None:
            task_name = task.get_name().strip()

        task_name_items = task_name.split(":")
        task_name_item= task_name_items[1].strip()

        test_str= "[REPORT]"
        if task_name_item.startswith( test_str ):
            task_name= task_name_items[0].strip()+" : "+task_name_item[len(test_str):]
            prefix="REPORT"

        return ""+str(prefix)+" ["+str(task_name)+" "+str(args)+"]"

    def obj_dump(self, obj):
            if self.debug is True:
                for attr in dir(obj):
                    if hasattr( obj, attr ):
                        print("obj."+str(attr)+" => "+str(getattr(obj, attr) ))

    def print_class_name(self):
        if self.debug is True:
            print ("== Current method is: "+self.print_stack_method())

    def print_stack_method(self):
        return inspect.stack()[2][3]

    def print_debug_result(self,result):
        if type(result._result) == dict and  self.debug is True:
            print("============  print_debug_result   ===============")
            print("item.keys():")
            print(result._result.keys())
            print("")
            print("item:")
            print(result._result)
            print("")
            print("type(item)")
            print(type(result._result))
            print("")

    @staticmethod
    def _get_task_module(result):
        r = ""
        try:
            r = result._task.action
        except:
            pass
        return r

    @staticmethod
    def _get_key(check_keys,items):
        """
        will search for the keys in the passed dict and return a csv string
        :param check_keys: str,list, dict
        :param items: dict, items to check in
        :return: str
        """

        return_str = ""
        checks = {}

        if isinstance(check_keys,str):
            checks = {check_keys: check_keys}
        elif isinstance(check_keys,list):
            for i in check_keys:
                checks[i] = i


        if isinstance(items, dict):
            item_keys = items.keys()
            # print(items)

            for check_key, check in checks.items():
                if check in item_keys:

                    data = ""
                    if isinstance(items[check], str):
                        data = items[check]
                    elif isinstance(items[check], int):
                        data = str(items[check])
                    elif isinstance(items[check], list):
                        data = ",".join(items[check])

                    return_str += " "+check_key+"="+data+","

        return return_str





    def get_filtered_item(self,result):

        action = self._get_task_module(result)
        host = result._host.get_name()
        keys = result._result.keys()
        items = result._result
        task_name = result.task_name or result._task

        handled_action = False

        ignored_action = [
            "setup",
            "reboot",
            "include_tasks",
            "raw",
            "cron",# for now
            "find",
            "stat",
            "include_vars",
            "set_fact",
        ]



        msg = ""
        if action in ignored_action:
            handled_action = True
        else:
            msg += " =>"

        if action != "":
            msg += " [Module:"+action+"]"

        # => SPECIFIC MODULES

        # APT
        if action == "apt":
            # self.print_debug_result(result)
            handled_action = True

            if "invocation" in keys:
                if "module_args" in items["invocation"]:
                    msg += self._get_key({"state":"state","pacakges":"name"},items["invocation"]["module_args"])


        # APT KEY
        if action == "apt_key":
            # self.print_debug_result(result)
            handled_action = True

            if "invocation" in keys:
                if "module_args" in items["invocation"]:
                    msg += self._get_key(["state","url"],items["invocation"]["module_args"])

        # apt_repository
        if action == "apt_repository":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key(["state","repo"],items)

        # Hostname
        if action == "hostname":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("name",items)

        # Command
        if action == "command" or action == "shell":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("cmd",items)

        # service
        if action == "service":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("name",items)

        # systemd
        if action == "systemd":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("name",items)

        # mysql_db
        if action == "mysql_db":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("db",items)

        # mysql_user
        if action == "mysql_user":
            # self.print_debug_result(result)
            handled_action = True
            msg += self._get_key("user",items)

        # mysql_replication
        if action == "mysql_replication":
            self.print_debug_result(result)
            handled_action = True

        # git
        if action == "git":
            # self.print_debug_result(result)
            # handled_action = True
            handled_action = True
            if "invocation" in keys:
                if "module_args" in items["invocation"]:
                    msg += self._get_key(["repo","dest"],items["invocation"]["module_args"])

        # pip
        if action == "pip":
            self.print_debug_result(result)
            # handled_action = True

        # blockinfile
        if action == "blockinfile":
            # self.print_debug_result(result)
            handled_action = True
            if "item" in keys:
                msg += self._get_key(["username","dest"],items["item"])

        # lineinfile
        if action == "lineinfile":
            # self.print_debug_result(result)
            handled_action = True
            if "invocation" in keys:
                if "module_args" in items["invocation"]:
                    msg += self._get_key(["dest","line"],items["invocation"]["module_args"])

        # File
        if action == "file":
            # self.print_debug_result(result)
            handled_action = True

            if "item" in keys:
                msg += self._get_key(["username"],items["item"])

            msg += self._get_key("path",items)

        # unarchive
        if action == "unarchive":
            self.print_debug_result(result)
            handled_action = True
            msg += self._get_key(["src","dest","state"],items)

        # get_url
        if action == "get_url":
            # self.print_debug_result(result)
            handled_action = True

            msg += self._get_key(["url","dest"],items)

        # user / group
        if action == "user" or action == "group":
            # self.print_debug_result(result)
            handled_action = True

            msg += self._get_key(["name","uid","gid"],items)

        # Copy
        if action == "copy":
            # self.print_debug_result(result)
            handled_action = True

            msg += self._get_key("dest",items)

        # template
        if action == "template":
            # self.print_debug_result(result)
            handled_action = True

            msg += self._get_key("dest",items)

        # fail
        if action == "fail":
            # self.print_debug_result(result)
            handled_action = True

            msg += self._get_key("msg",items)

        # debug
        if action == "debug":
            # self.print_debug_result(result)
            handled_action = True

            test_str= "[REPORT]"
            if task_name.startswith( test_str ) and  "msg" in keys:
                report_msg = "["+host+"] [Module:debug] => "+items["msg"]
                self.add_to_report(report_msg,t="msg",task=self.crete_task_banner(result._task))

        # => END SPECIFIC MODULES

        if "skip_reason" in keys:
            msg += " skip_reason="+items["skip_reason"]

        if handled_action == False and self.debug == True:
            report_msg = "["+host+"] => Unhandled module: "+action+ " in get_filtered_item()"
            self.add_to_report(report_msg,t="msg",task="Unhandled module : "+action)

        return msg

    def v2_runner_on_failed(self, result, ignore_errors=False):

        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        self._clean_results(result._result, result._task.action)

        if self._last_task_banner != result._task._uuid:
            self._print_task_banner(result._task)

        self._handle_exception(result._result, use_stderr=self.display_failed_stderr)
        self._handle_warnings(result._result)

        if result._task.loop and 'results' in result._result:
            self._process_items(result)
            msg = "somehow fatal:"

        else:
            if delegated_vars:
                msg = "fatal: [%s -> %s]: FAILED! => %s" % (result._host.get_name(), delegated_vars['ansible_host'], self._dump_results(result._result) )
                # msg += self.get_filtered_item(result)
            else:
                msg= "fatal: [%s]: FAILED! => %s" % (result._host.get_name(), self._dump_results(result._result))
                # msg += self.get_filtered_item(result)



            self._display.display(msg, color=C.COLOR_ERROR, stderr=self.display_failed_stderr)

        if ignore_errors:
            self._display.display("...ignoring", color=C.COLOR_SKIP)
        else:
            self.add_to_report(msg[len("fatal:"):],t="fatal",task=self.crete_task_banner(result._task))


    def v2_runner_on_ok(self, result):
        is_changed = False

        delegated_vars = result._result.get('_ansible_delegated_vars', None)

        if isinstance(result._task, TaskInclude):
            return
        elif result._result.get('changed', False):
            is_changed = True
            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            if delegated_vars:
                msg = "changed: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
            else:
                msg = "changed: [%s]" % result._host.get_name()
                msg += self.get_filtered_item(result)

            color = C.COLOR_CHANGED

        else:
            if not self.display_ok_hosts:
                return

            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            if delegated_vars:
                msg = "ok: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
            else:
                msg = "ok: [%s]" % result._host.get_name()
                msg += self.get_filtered_item(result)
            color = C.COLOR_OK

        self._handle_warnings(result._result)

        if is_changed:
            self.add_to_report(msg[len("changed:"):],t="changed",task=self.crete_task_banner(result._task))

        if result._task.loop and 'results' in result._result:
            self._process_items(result)

        else:
            self._clean_results(result._result, result._task.action)
            if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                msg += " => %s" % (self._dump_results(result._result),)

            # if is_changed:
            #     print("===========================BINGO")
            #     self.add_to_report(msg[len("changed:"):],t="changed",task=self.crete_task_banner(result._task))

            self._display.display(msg, color=color)

    def v2_runner_on_skipped(self, result):

        if self.display_skipped_hosts:

            self._clean_results(result._result, result._task.action)

            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            if result._task.loop and 'results' in result._result:
                self._process_items(result)
            else:
                msg = "skipping: [%s]" % result._host.get_name()
                msg += self.get_filtered_item(result)

                if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                    msg += " => %s" % self._dump_results(result._result)
                self._display.display(msg, color=C.COLOR_SKIP)


    def v2_runner_item_on_failed(self, result):
        if self._last_task_banner != result._task._uuid:
            self._print_task_banner(result._task)

        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        self._clean_results(result._result, result._task.action)
        self._handle_exception(result._result)

        msg = "failed: "
        if delegated_vars:
            msg += "[%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
        else:
            msg += "[%s]" % (result._host.get_name())

        msg += self.get_filtered_item(result)

        if "_ansible_ignore_errors" in result._result.keys() and result._result["_ansible_ignore_errors"] == True:
            ignore_report = True
        else:
            ignore_report = False

        if not ignore_report:
            self.add_to_report(msg[len("failed:"):],t="failed",task=self.crete_task_banner(result._task))

        self._handle_warnings(result._result)
        self._display.display(msg + " (item=%s) => %s" % (self._get_item_label(result._result), self._dump_results(result._result)), color=C.COLOR_ERROR)

    def v2_runner_item_on_ok(self, result):

        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        self._clean_results(result._result, result._task.action)
        if isinstance(result._task, TaskInclude):
            return
        elif result._result.get('changed', False):
            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            msg = 'changed'
            color = C.COLOR_CHANGED
        else:
            if not self.display_ok_hosts:
                return

            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            msg = 'ok'
            color = C.COLOR_OK

        if delegated_vars:
            msg += ": [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
        else:
            msg += ": [%s]" % result._host.get_name()

        # msg += " => (item=%s)" % (self._get_item_label(result._result),)
        msg += self.get_filtered_item(result)

        if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
            msg += " => %s" % self._dump_results(result._result)
        self._display.display(msg, color=color)



    def v2_runner_item_on_skipped(self, result):
        """
        When running on an iteration over items e.g with_items
        :param result:
        :return:
        """
        if self.display_skipped_hosts:
            if self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            self._clean_results(result._result, result._task.action)
            # msg = "skipping: [%s] => (item=%s) " % (result._host.get_name(), self._get_item_label(result._result))

            msg = "skipping: [%s]" % result._host.get_name()
            msg += self.get_filtered_item(result)

            if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                msg += " => %s" % self._dump_results(result._result)

            self._display.display(msg, color=C.COLOR_SKIP)






    def print_section(self,msg):
        import os
        rows, columns = os.popen('stty size', 'r').read().split()
        s = "#"
        d = "=" * (int(columns) -1)
        print("")
        print(s+d)
        print(s+" "+str(msg))
        print(s+d)

    #============================================================================================================
    # Enroll system
    #============================================================================================================

    def v2_playbook_on_stats(self, stats):
        self.print_section("CHANGELOG")
        # extend with printing change report

        # print(self.report)
        if len(self.report) > 0:
            report_banner = ""

            for item in self.report:

                if item["task"] != "" and item["task"] != report_banner :
                    # print(item["task"])
                    self._display.banner(item["task"])
                    report_banner = item["task"]

                data =  item["data"]
                if isinstance(item["data"],list):
                    data = "\n"
                    data += '\n'.join(item["data"])

                host_str = ""
                if item["host"] !="":
                    host_str += " ["+item["host"]
                    if item["task"] != "":
                        host_str += " :: "+item["task"]
                    host_str += "] => "

                if item["t"]=="msg":
                    self._display.display("msg:"+host_str+"=> "+data, color=C.COLOR_SKIP)
                elif item["t"] == "changed":
                    self._display.display("changed:"+host_str+data, color=C.COLOR_CHANGED)
                elif item["t"] == "failed":
                    self._display.display("failed:"+host_str+data, color=C.COLOR_ERROR)
                elif item["t"] == "fatal":
                    self._display.display("fatal:"+host_str+data, color=C.COLOR_ERROR)

        else:
            self._display.display("The report does not contain changes", color=C.COLOR_OK)



        self.print_section("PLAY RECAP")
        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)

            self._display.display(u"%s : %s %s %s %s %s" % (
                hostcolor(h, t),
                colorize(u'ok', t['ok'], C.COLOR_OK),
                colorize(u'changed', t['changed'], C.COLOR_CHANGED),
                colorize(u'unreachable', t['unreachable'], C.COLOR_UNREACHABLE),
                colorize(u'failed', t['failures'], C.COLOR_ERROR),
                colorize(u'skipped', t['skipped'], C.COLOR_SKIP)),
                                  screen_only=True
                                  )

            self._display.display(u"%s : %s %s %s %s %s" % (
                hostcolor(h, t, False),
                colorize(u'ok', t['ok'], None),
                colorize(u'changed', t['changed'], None),
                colorize(u'unreachable', t['unreachable'], None),
                colorize(u'failed', t['failures'], None),
                colorize(u'skipped', t['skipped'], None)),
                                  log_only=True
                                  )

        self._display.display("", screen_only=True)

        # print custom stats if required
        if stats.custom and self.show_custom_stats:
            self._display.banner("CUSTOM STATS: ")
            # per host
            # TODO: come up with 'pretty format'
            for k in sorted(stats.custom.keys()):
                if k == '_run':
                    continue
                self._display.display('\t%s: %s' % (k, self._dump_results(stats.custom[k], indent=1).replace('\n', '')))

            # print per run custom stats
            if '_run' in stats.custom:
                self._display.display("", screen_only=True)
                self._display.display('\tRUN: %s' % self._dump_results(stats.custom['_run'], indent=1).replace('\n', ''))
            self._display.display("", screen_only=True)

