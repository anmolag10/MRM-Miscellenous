int sw=2;
int xaxis=A0;
int yaxis=A1;
int FrontR=11;
int FrontL=10;
int BackR=9;
int BackL=6;
int xmapped,lval,rval,x,y;
const int vmax=255;
void setup() { 
 pinMode(sw,INPUT);
 pinMode(xaxis,INPUT);
 pinMode(yaxis,INPUT);
 pinMode(FrontR,OUTPUT);
 pinMode(FrontL,OUTPUT);
 pinMode(BackR,OUTPUT);
 pinMode(BackL,OUTPUT);
 Serial.begin(9600);
}
void loop() {
digitalWrite(sw,HIGH);
x=analogRead(xaxis);
y=analogRead(yaxis);


if((y==512 || x=512)) // to check if it is origin // to be calibrated accordingly
{ 
  rval=0;
  lval=0;
}
else if(y>512) // above origin to move forward
{
  rval=map(y,512,1023,0,255);
  lval=map(y,512,10230,0,255);
}
else if(y<512) // below origin to move backward
{
  rval=map(y,512,0,0,-255);
  lval=map(y,512,0,0,-255);
}
// mapping xAxis to get exact analogWrite value
{ 

if(x>512) 
{
  xmapped=map(x,512,1023,0,255);
  rval=rval+xmapped;
  lval=lval-xmapped;
}
else if(x<512)
{ 
  xmapped=map(x,512,0,0,255);
  rval=rval+xmapped;
  lval=lval-xmapped;
}
if(rval<0)
{ 
  analogWrite(BackR,abs(rval));
}
else
{
  analogWrite(FrontR,rval);
}
if(lval<0)
{
 analogWrite(BackL,abs(lval));
}
else
 analogWrite(FrontL,lval);

 Serial.print('The xAxis: ');
 Serial.print(x);
 
 Serial.print('The yAxis: ');
 Serial.print(y);
 
}

        
.
        
