float CurColor=0;
float2 NewUV = UV;
int i=0;
float StepSize = Distance / (int) DistanceSteps;
float CurDistance=0;
float2 CurOffset=0;
float SubOffset = 0;
float TwoPi = 6.283185;

float DefaultDepth = CalcSceneDepth(UV);

float Steps = 1;

if (DistanceSteps < 1)
{
  return DefaultDepth;
}
else
{
  while (i < (int) DistanceSteps)
  { 
    CurDistance += StepSize; 
    for (int j = 0; j < (int) RadialSteps; j++) 
    {
      SubOffset +=1;
      CurOffset.x = cos(TwoPi*(SubOffset / RadialSteps));
      CurOffset.y = sin(TwoPi*(SubOffset / RadialSteps)); 
      NewUV.x = UV.x + CurOffset.x * CurDistance; 
      NewUV.y = UV.y + CurOffset.y * CurDistance; 
      CurColor += (DefaultDepth - CalcSceneDepth(NewUV)) * pow(Steps, KernelPower);
    }
    Steps -= 1/DistanceSteps;
    i++;
  }
  return CurColor;
}