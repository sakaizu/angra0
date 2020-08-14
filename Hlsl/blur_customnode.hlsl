float3 blur = Texture2DSample(SceneColorTexture, SceneColorTextureSampler, uv).rgb;
float Inputpower = 1;
float str = Inputpower*0.1;
int i;

for (int i = 0; i < n; i++)
{

	blur += Texture2DSample(SceneColorTexture, SceneColorTextureSampler, float2 (uv.x, uv.y - str)).rgb;
	str += Inputpower*0.1;

	blur += Texture2DSample(SceneColorTexture, SceneColorTextureSampler, float2 (uv.x, uv.y - str)).rgb;
	str += Inputpower*0.1;

}

blur /= n * 2 + 1;

return blur;