float3 SceneColor;
float2 NewUV;
float2 BaseUV;
float TwoPi = 6.283185;
float2 Offset;
float SubStep;
const int TexIndex = 14;

BaseUV = ViewportUVToSceneTextureUV(UV,14);
NewUV = ViewportUVToSceneTextureUV(UV,14);

if(Count <= 0)
{
return DecodeSceneColorForMaterialNode(UV);
}
else
{
for(int i =0; i<Count; i++)
 {
    Offset.x = cos(TwoPi*(SubStep / Count));
    Offset.y = sin(TwoPi*(SubStep / Count));
    SceneColor += SceneTextureLookup(NewUV, TexIndex, false);
    NewUV = BaseUV + (Offset * (Length + TempAA));
    SubStep++;
}
}
return SceneColor/Count;