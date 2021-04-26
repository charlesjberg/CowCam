t = tcpclient('localhost',50007, 'ConnectTimeout', 100);
data = uint8(1:10);
write(t, data)
data_echo = read(t, 18);
char(data_echo)
clear t

