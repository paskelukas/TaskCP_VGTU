#!/bin/bash


instance="$1"
pathSCF="/native"
environment="$2"
ldapUsername="$3"
passwd="$4"
errors=0


# -- Create the download file location --

mkdir runtime-${instance}
cd runtime-${instance}

# -- Request ldap and  password --

# echo -e "\n"
# read -p "Please enter your ldap: " ldapUsername
# echo -e "\n"
# read -s -p "Please enter your password: " passwd
# echo -e "\n"

# -- Connect to sftp and download the file --


export SSHPASS=${passwd}
sshpass -e sftp -oBatchMode=no -b - ${ldapUsername}@sftp.bazaarvoice.com << !
   cd ${instance}/native
   ls *${instance}_standard_client_feed*.xml
   get *${instance}_standard_client_feed*.xml
   exit
!




# gzip -dk *${instance}_standard_client_feed*.xml.gz
echo *${instance}_standard_client_feed*.xml
cd ..

# python3 num_of_content.py runtime-${instance}/*${instance}_standard_client_feed*.xml

# -- Remove the downloaded file and the folder --

# cd runtime-${instance}
# rm *${instance}_standard_client_feed*.xml*
# cd ..
# rmdir runtime-${instance}

