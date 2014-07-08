#!/bin/bash 
set -x 

while [ 1 -eq 1 ]
do 
 read filename 

 echo $filename  |grep http 
 is_filename_url=$?


 if [[ $is_filename_url  -eq 0 ]];
 then 
	# extract the filename and assign 
	extracted_filename=$(	basename $filename  ) 
	if [ ! -f $extracted_filename ]  ; 
	then 
		#download the file to disk 
		wget "$filename" ; 

		if [[ $? -ne 0 ]]; 
		then 
		 exit 
		fi 	

	fi 


	# to filename below 
	filename=$extracted_filename
	
 fi

# Run the binary with the filename  
	./test.py $filename


done  

