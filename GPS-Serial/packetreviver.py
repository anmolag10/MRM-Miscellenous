import time
import serial
ser = serial.Serial('/dev/ttyS0')
ser.flushInput()

while True:
    try:
        # time.sleep(0.01)
        ser_bytes = ser.read(10)
        decode = str(ser_bytes.decode('utf-8'))
        try:
          for ch in data:
           if ch in ('p','n','a','m'):
            if ch=='p':
                i=data.index(ch)
                lval=data[i+1:i+4]
                print(lval)
            if ch=='n':
                i=data.index(ch)
                lval=int(data[i+1:i+4])*(-1)
                print(lval)
            if ch=='a':
                i=data.index(ch)
                rval=data[i+1:i+4]
                print(rval)
            if ch=='m':
                i=data.index(ch)
                rval=int(data[i+1:i+4])*(-1)
                print(rval)
        except:
            pass
    except:
        break
        
