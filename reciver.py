import Serial
packet = str()
started = False
while True:
    ch = ''
    if (Serial.available() > 0):
      ch= Serial.read()
    if (ch == 's'):
      started = True
    elif (character == 'e') {
      started = False
      packet=''
      
    if (started == True):
      packet += ch

    if (packet.length() == 8):
      lval = packet[0];
      rval = packet[4];
    print('Lval',lval)
    print('Rval',)rval