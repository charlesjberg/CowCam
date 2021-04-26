echoudp('on',4015)
u = udp('127.0.0.1',4015, 'Timeout',1);
fopen(u)
fwrite(u,1:10)
A = fread(u,10)
echoudp('off')
fclose(u)

