import paramiko
################################# Transfer file from Remote server (Linux here) to local server (windows here) #################################
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # This is to add the host to the known host list and avoids asking the prompt 'Yes' or 'No'
# ssh.connect(hostname='56.165.97.91',username='ec2-user',password='paramiko123',port=22)
ssh.connect(hostname='106.206.79.116',username='root',password='cunning',port=22)
sftp_client=ssh.open_sftp() # This opens the sftp client

sftp_client.get('/home/ubuntu/test1.txt','paramiko_downloaded_file.txt') # Get is used to download the file, source path and local path, Here Local server is windows
# and remote server is Linux

sftp_client.close() # Closing the sftp client
ssh.close() # Closing the ssh client, make sure you close ssh client after the sftp client because sftp uses ssh

################################# to change the directory and fetch the files from remote ###################################################
# sftp_client.chdir("/home/ec2-user")
# print(sftp_client.getcwd())
# sftp_client.get('demo.txt','C:\\Users\\Automation\\Desktop\\download_file.txt')
# sftp_client.close()
# ssh.close()

################################################### Transfer file from Local (windows) to Remote (Linux) ###################################################
# sftp_client.put('paramiko_to_transfer_file.txt','/home/ec2-user/received_file.txt')
# sftp_client.close()
# ssh.close()