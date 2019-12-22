#!/usr/bin/env bash
command -v whiptail >/dev/null 2>&1 || { echo >&2 "whiptail is required but it's not installed.  Aborting."; exit 1; }


if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi


Avaliable="/etc/nginx/sites-available/"
Enabled="/etc/nginx/sites-enabled/"

PRINT="";
#ENABLEDSITES=($(ls $Enabled*.conf))
ENABLEDSITES=($(find $Enabled -type l -not -name "*.*~"))



#for file in `ls $Avaliable *.conf`
for file in `find $Avaliable -type f -not -name "*.*~"`
do
    filename=`basename $file`;
    PRINT="$PRINT $filename"


    check="$Enabled$filename"
    if [ -f $check ];
    then
       PRINT="$PRINT [ON] ON"
    else
       PRINT="$PRINT [OFF] OFF"
    fi
done


COLS=`tput cols`
ROWS=`tput lines`

ROWS=$(($ROWS-4))
ROWS2=$(($ROWS-8))

CHANGES=false;
SITES=$(whiptail --title "Enable Sites" --checklist "Select the sites to enable:" $ROWS 70 $ROWS2 $PRINT 3>&1 1>&2 2>&3)


exitstatus=$?

if [ $exitstatus = 0 ]; then
#    echo "Your selected sites are:" $SITES

    echo ""
    echo "###########################################################################"
    echo "## changes Made"
    echo "###########################################################################"


    SITESARRAY=();
    echo "Enable:"
    for site in $SITES # note that $var must NOT be quoted here!
    do
        site="${site%\"}"
        site="${site#\"}"

        check="$Enabled$site"
        SITESARRAY+=($check)
        if [ ! -f $check ];
        then
           echo "  $site"
           d=`ln -s $Avaliable$site $Enabled$site`
           CHANGES=true
        fi
    done

    echo "Disable:"
    for site in "${ENABLEDSITES[@]}"
    do
        if [[  ! " ${SITESARRAY[@]} " =~ " ${site} " ]]; then
            filename=`basename $site`;
            echo "  $filename"
            rm "$site"
            CHANGES=true
        fi
    done



    if [ "$CHANGES" = true ] ; then


        echo ""
        echo "###########################################################################"
        echo "## nginix -t"
        echo "###########################################################################"

        nginxTest=`nginx -t`
        ret_code=$?
        echo ""


        if [ "$ret_code" = 0 ] ; then

#            LOOP="true"
#            while [ "$LOOP" == "true" ]; do
                echo ""
                echo "###########################################################################"
                echo "## reload Nginx"
                echo "###########################################################################"
                echo    "You need to reload or restart nginx to have the changes take effect."

                read -p "Do you want to do reload now (Y/n)" -n 1 -r
                echo ""
                if [[ $REPLY =~ ^[Yy]$ ]] || [[ ${#REPLY} -eq 0 ]]
                then
                    echo "reloading Nginx config"
                    d=`service nginx reload`
                fi
#            done
        fi
    fi




else
    exit
fi




