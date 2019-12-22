#!/usr/bin/env bash
command -v whiptail >/dev/null 2>&1 || { echo >&2 "whiptail is required but it's not installed.  Aborting."; exit 1; }

certDir="/etc/letsencrypt"

function printHelp(){
echo "actions:"
echo "  · list"
echo "  · delete <certname>"
}

function listCerts(){
        ls -l "$certDir/live"
}

function delete(){
        echo "delete: $1"

        echo "rm -R $certDir/live/$1"
        rm -R $certDir/live/$1

        echo "rm -R $certDir/archive/$1"
        rm -R $certDir/archive/$1

        echo "rm $certDir/renewal/$1.conf"
        rm $certDir/renewal/$1.conf


}
#############################################################################################################################
## END of FUNCTIONS
#############################################################################################################################

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

echo "  = Letsencrypt certificate delete = "

DIR=$(pwd)

if [ -z "$1" ]
  then
    printHelp;
fi

if [ "$1" == "list" ]; then
        listCerts;
fi

if [ "$1" == "delete" ]; then
        if [ -z "$2" ]; then
                printHelp;
        else
                delete $2;
        fi
fi
exit;
