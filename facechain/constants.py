neg_prompt = '(nsfw:2), paintings, sketches, (worst quality:2), (low quality:2), ' \
             'lowers, normal quality, ((monochrome)), ((grayscale)), logo, word, character, bad hand, tattoo, (username, watermark, signature, time signature, timestamp, artist name, copyright name, copyright),'\
             'low res, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, strange fingers, bad hand, mole, ((extra legs)), ((extra hands))'
pos_prompt_with_cloth = 'raw photo, masterpiece, chinese, {}, solo, medium shot, high detail face, looking straight into the camera with shoulders parallel to the frame, slim body, photorealistic, best quality'
pos_prompt_with_style = '{}, upper_body, raw photo, masterpiece, solo, medium shot, high detail face, slim body, photorealistic, best quality'

base_models = [
    {'name': 'leosamsMoonfilm_filmGrain20',
    'model_id': 'ly261666/cv_portrait_model',
    'revision': 'v2.0',
    'sub_path': "film/film",
    'style_list': ['工作服(Working suit)', '盔甲风(Armor)','T恤衫(T-shirt)','汉服风(Hanfu)','女士晚礼服(Gown)','赛博朋克(Cybernetics punk)','凤冠霞帔(Chinese traditional gorgeous suit)','休闲生活风(Casual Lifestyle)','梅花女孩(Chinese Girl among Plum Blossoms)','芭比娃娃(Barbie Doll)','白月光(Innocent Girl in White Dress)','优雅公主(Elegant Princess)','鬼马少女(Pixy Girl)']},
    {'name': 'MajicmixRealistic_v6',
    'model_id': 'YorickHe/majicmixRealistic_v6',
    'revision': 'v1.0.0',
    'sub_path': "realistic",
    'style_list': ['冬季汉服(Chinese winter hanfu)', '校服风(School uniform)', '婚纱风(Wedding dress)', '夜景港风(Hong Kong night style)', '雨夜(Rainy night)', '模特风(Model style)', '机车风(Motorcycle race style)', '婚纱风-2(Wedding dress 2)','拍立得风(Polaroid style)', '仙女风(Fairy style)', '古风(traditional chinese style)', '壮族服装风(Zhuang style)', '欧式田野风(European fields)', '雪山羽绒服风(Jacket in Snow Mountain)', '旗袍风(Cheongsam)', '日系和服风(Kimono Style)', '贵族公主风(Princess costum)','机械风(Mechanical)','林中鹿女风(deer girl)','漫画风(cartoon)']},
]

styles = [
    {'name': '工作服(Working suit)',
     'img': './style_image/Working_suit.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing high-class business/working suit, simple background, high-class pure color background'},
    {'name': '盔甲风(Armor)',
     'img': './style_image/Armor.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing silver armor, simple background, high-class pure color background'},
    {'name': 'T恤衫(T-shirt)',
     'img': './style_image/T-shirt.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing T-shirt, simple background, high-class pure color background'},
    {'name': '汉服风(Hanfu)',
     'img': './style_image/Hanfu.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing beautiful traditional hanfu, upper_body, simple background, high-class pure color background'},
    {'name': '女士晚礼服(Gown)',
     'img': './style_image/Gown.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing an elegant evening gown, simple background, high-class pure color background'},
    {'name': '赛博朋克(Cybernetics punk)',
     'img': './style_image/Cybernetics_punk.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'white hair, neon glowing glasses, cybernetics, punks, robotic, AI, NFT art, Fluorescent color, ustration'},
    {'name': '凤冠霞帔(Chinese traditional gorgeous suit)',
     'img': './style_image/Chinese_traditional_gorgeous_suit.jpg',
     'model_id': 'ly261666/civitai_xiapei_lora',
     'revision': 'v1.0.0',
     'bin_file': 'xiapei.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'red, hanfu, tiara, crown'},
     {'name': '冬季汉服(Chinese winter hanfu)',
     'img': './style_image/Chinese_winter_hanfu.jpg',
     'model_id': 'YorickHe/Winter_hanfu_lora',
     'revision': 'v1.0.0',
     'bin_file': 'Winter_Hanfu.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': 'red hanfu, winter hanfu, cloak, photography, warm light, sunlight, majestic snow scene,  close-up, front view, soft falling snowflakes, jewelry, enchanted winter wonderland'},
     {'name': '校服风(School uniform)',
     'img': './style_image/School_uniform.jpg',
     'model_id': 'YorickHe/JK_uniform_lora',
     'revision': 'v1.0.0',
     'bin_file': 'jk_uniform.safetensors',
     'multiplier_style': 0.2,
     'multiplier_human': 0.95,
     'add_prompt_style': 'JK_style, white short-sleeved JK_shirt, dark blue JK_skirt, bow JK_tie, close-up, looking at viewer, sweet smile, night, Tokyo street, night city scape'},
     {'name': '婚纱风(Wedding dress)',
     'img': './style_image/Wedding_dress.jpg',
     'model_id': 'YorickHe/outdoor_photo_lora',
     'revision': 'v1.0.0',
     'bin_file': 'outdoor_photo_v2.0.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': 'white wedding dress, 1girl, summer, flower, happy atmosphere, sunlight, Waist Shot'},
     {'name': '夜景港风(Hong Kong night style)',
     'img': './style_image/Hong_Kong_night_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, face shot, stylish outfit, fitted jeans, oversized jacket, fashionable accessories, cityscape backdrop, rooftop or high-rise balcony, dynamic composition, engaging pose, soft yet striking lighting, shallow depth of field, bokeh from city lights, naturally blurred background'},
     {'name': '雨夜(Rainy night)',
     'img': './style_image/Rainy_night.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.45,
     'multiplier_human': 0.95,
     'add_prompt_style': 'standing in the rain, wet, wet clothes, wet hair, face Shot, front view, close-up, cityscape, cold lighting, realistic, cinematic lighting, photon mapping, radiosity, physically-based rendering'},
     {'name': '模特风(Model style)',
     'img': './style_image/Model_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, balenciaga, close-up, fashion, streets of new york, new york, modeling for Balenciaga, natural skin texture, dynamic pose, rouge, film grain'},
     {'name': '机车风(Motorcycle race style)',
     'img': './style_image/Motorcycle_race_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, wearing racing clothes, motorbike clothes, modeling, playful, futuristic, city street background, at night, cool atmospheric, realistic'},
     {'name': '婚纱风-2(Wedding dress 2)',
     'img': './style_image/Wedding_dress_2.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, wearing wedding dress, white, film grain, sunlight, sun flare, lens flare, field of white roses, high fashion, top model'},
    {'name': '拍立得风(Polaroid style)',
     'img': './style_image/Polaroid_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, simple clothes, front view, looking straight into the camera, film grain, flash, enhanced flash, dark background, polaroid, instant photo, realistic face'},
     {'name': '仙女风(Fairy style)',
     'img': './style_image/Fairy_style.jpg',
     'model_id': 'YorickHe/fairy_lora',
     'revision': 'v1.0.0',
     'bin_file': 'fairy.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'a beautiful fairy standing in the middle of a flower field, petals, close-up, warm light, light green atmosphere, white atmosphere, in the style of celebrity photography, soft, romantic scenes, flowing fabrics, light white and light orange, high resolution'},
     {'name': '古风(traditional chinese style)',
     'img': './style_image/traditional_chinese_style.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'MoXinV1.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': '(best quality, hanfu, Chinese traditional ink painting:1.8), close-up, song, anxiang, chinese_clothes, ornaments, topknot, perfect eyes, perfect face, soft smile'},
    {'name': '壮族服装风(Zhuang style)',
     'img': './style_image/Zhuang_style.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'zhuangnv.safetensors',
     'multiplier_style': 0.75,
     'multiplier_human': 0.95,
     'add_prompt_style': '((best quality)), close-up, portrait, ((zhuangzunv)), ornaments, jewelry, headwear, ((beautiful embroidery, floral print, marvelous design)), perfect eyes, perfect face, gentle black hair, smile'},
    {'name': '欧式田野风(European fields)',
     'img': './style_image/European_fields.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'edgEuropean_Vintage.safetensors',
     'multiplier_style': 0.55,
     'multiplier_human': 0.95,
     'add_prompt_style': 'focused, (edgEV, wearing edgEV_vintage dress), (field, natural lighting, detailed background, cinematic lighting), (gentle hair:1.1), windy hair, perfect eyes, perfect face'},
    {'name': '雪山羽绒服风(Jacket in Snow Mountain)',
     'img': './style_image/Jacket_in_Snow_Mountain.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v7',
     'bin_file': 'puffy_jacket-1.0.safetensors',
     'multiplier_style': 0.6,
     'multiplier_human': 0.9,
     'add_prompt_style': 'close-up, fur collar, ((jacket)), shirt, pants, winter, (bright sunny day, snow mountain, alpine slopes, snow), gyaru, fashion, trendy, gentle hair'},
    {'name': '旗袍风(Cheongsam)',
     'img': './style_image/Cheongsam.jpg',
     'model_id': 'PaperCloud/zju19_minguo_style_lora',
     'revision': 'v1.0.0',
     'bin_file': 'qipao2.safetensors',
     'multiplier_style': 0.45,
     'multiplier_human': 0.95,
     'add_prompt_style': 'white_cheongsam, photography, warm light, Chinese classical indoor scene, close-up, front view, earrings, hairpin, serenity, elegant, facing the camera with a smile, beautiful chinese embroidery, symmetrical short sleeves'},
    {'name': '日系和服风(Kimono Style)',
     'img': './style_image/Kimono.jpg',
     'model_id': 'ZackWang123/filmvelvia_lora',
     'revision': 'v1.0.0',
     'bin_file': 'FilmVelvia3.safetensors',
     'multiplier_style': 0.45,
     'multiplier_human': 0.95,
     'add_prompt_style': 'outdoor, (linen:1.4), cute japanese model girl, kimono, floral print, hair ornament, looking at viewer, hair flower, brown eyes, bangs, realistic'},
    {'name': '贵族公主风(Princess costum)',
     'img': './style_image/Princess_style.jpg',
     'model_id': 'AzilyModelScope/facechain_lora',
     'revision': 'v1.0.0',
     'bin_file': 'foreign_princess_costum.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'fantasy girl, close-up, Waist shot, long hair, jewelry, earrings, looking at viewer, white dress, cathedral background, crown, (detailed face, perfect face, perfect eyes, realistic eyes), (clear face), high detail, sharp focus, dramatic, beautiful girl'},
    {'name': '机械风(Mechanical)',
     'img': './style_image/Mechnical.jpg',
     'model_id': 'rewfueranro/Mechanical_lora',
     'revision': 'v1.0.0',
     'bin_file': 'reelmech1v2.safetensors',
     'multiplier_style': 1,
     'multiplier_human': 0.95,
     'add_prompt_style': 'looking to the camera , clean face, Masterpiece, top quality, official art, beautiful and aesthetic, a full portrait of a futuristic dystopian city,  scrapper,  intricate, elegant, highly detailed, sharp focus,  cyberpunk, luminescence: 1.3, transparency,  8K, stunning art, digital photography, painting, hyper-realistic art: 1.3, mechanical woman, art by Genevieve Valentine: 1.2, Nikon D850, F/8, reelmech, demonic, expressive, hypnotic, delicate, moody, alluring, perfect shading, HDR, photorealistic: 1.6'},
    {'name': '林中鹿女风(deer girl)',
     'img': './style_image/Deer_girl.jpg',
     'model_id': 'EnlZhao/deer_lora',
     'revision': 'v3.2.0',
     'bin_file': 'deer.safetensors',
     'multiplier_style': 0.5,
     'multiplier_human': 0.95,
     'add_prompt_style': 'bust shot, an elk girl in pink forest, smile, keep eyes staring at the camera, detailed antlers, monochrome ears, white dress, slim body, long hair, natural lighting, warm sunlight, light pink atmosphere, outdoor photo, field of pink maple leaves, flower, realistic, best quality'},
    {'name': '漫画风(cartoon)',
     'img': './style_image/cartoon.jpg',
     'model_id': 'rewfueranro/cartoon_lora',
     'revision': 'v1.0.0',
     'bin_file': 'cartoon.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'Manhuanan,jewelry,1boy,<lora:Manhuanan_20230827182922-000009:1>,half body photo,white hair,at the coffee shop,blurred background,CG,UE5'},
    {'name': '休闲生活风(Casual Lifestyle)',
     'img': './style_image/Casual_Lifestyle.jpg',
     'model_id': 'theRealSlimShady/AI_portraits',
     'revision': 'v2',
     'bin_file': 'PortaitMasterV1.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'smile, lips, put on makeup, wearing casual clothes, simple background, blurred background'},
    {'name': '梅花女孩(Chinese Girl among Plum Blossoms)',
     'img': './style_image/Chinese_Girl_among_Plum_Blossoms.jpg',
     'model_id': 'theRealSlimShady/AI_portraits',
     'revision': 'v2',
     'bin_file': 'edgFae_FINAL.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.9,
     'add_prompt_style': 'chinese, wearing traditional chinese clothes, plum blossoms, wearing florescent makeup'},
    {'name': '芭比娃娃(Barbie Doll)',
     'img': './style_image/Barbie_Doll.jpg',
     'model_id': 'theRealSlimShady/AI_portraits',
     'revision': 'v2',
     'bin_file': 'PinkBarbie.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'golden blond hair, wearing frilly dress, bow and ponytail, exquisite background, pure color background, delicate earrings and necklace, solo, happy expression'},
    {'name': '白月光(Innocent Girl in White Dress)',
     'img': './style_image/Innocent_Girl_in_White_Dress.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing elegant white dress, simple pure color background, face located in the center of the picture, long black hair, inquisitive eyes, innocent expression, lips'},
    {'name': '优雅公主(Elegant Princess)',
     'img': './style_image/Elegant_Princess.jpg',
     'model_id': 'theRealSlimShady/AI_portraits',
     'revision': 'v2',
     'bin_file': 'blancanievesV2.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'short black wavy hair, pale complexion, white lace, sky-blue dress, puff sleeves, earings, necklace, happy expression, simple pure color background'},
    {'name': '鬼马少女(Pixy Girl)',
     'img': './style_image/Pixy_Girl.jpg',
     'model_id': 'theRealSlimShady/AI_portraits',
     'revision': 'v2',
     'bin_file': 'VidiaTinkerbellDisney-08.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'purple hair, ponytail, wearing slip skirt,looking straight into the camera with shoulders parallel to the frame, light purple background'},
    {'name': '复古风(Retro Style)',
     'img': './style_image/Retro_style.jpg',
     'model_id': 'HanYixuan1/Retro_style',
     'revision': 'v1.0.0',
     'bin_file': 'Retro_style.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.8,
     'add_prompt_style': '1990s, <lora:RetroFusion v1.0.0:1>,  1girl, woman looking out window, against glass, clothes,gray white and black ,black hair,misty beauty,glimmer,warm-toned,soft,sense of depth，Gauze texture，Solid fabric，low pixel，thin， face focusing，rough cloth，fit，Slight yellowing，autochrome photography，light and shade  contrast，dim，pale，color fading，Monastic dress，Drop hands naturally，no hands，Exclude hands，Blur the old city background'},
]

pose_models = [
    {'name': '无姿态控制(No pose control)'},
    {'name': 'pose-v1.1-with-depth'},
    {'name': 'pose-v1.1'}
]

pose_examples = {
    'man': [
        ['./poses/man/pose1.png'],
        ['./poses/man/pose2.png'],
        ['./poses/man/pose3.png'],
        ['./poses/man/pose4.png']
    ],
    'woman': [
        ['./poses/woman/pose1.png'],
        ['./poses/woman/pose2.png'],
        ['./poses/woman/pose3.png'],
        ['./poses/woman/pose4.png'],
    ]
}
