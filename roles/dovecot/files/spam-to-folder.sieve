require ["fileinto","mailbox","imap4flags"];

if header :contains "X-Spam-Flag" "YES" {
  setflag "\\Seen";
  fileinto :create "\Spam";
  stop;
}

