import requests

source = {
  'output_format': 'mp4',
  'frame_rate': 30,
  'width': 1080,
  'height': 1080,
  'elements': [

    # Image 1
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/image_4a1fe76f-8d4d-4274-9130-fb22dadf1e73.jpg?v=1635099109',
      'animations': [
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '50%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '50%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 2
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/WhatsAppImage2022-05-11at1.20.03AM.jpg?v=1652215859',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '100%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '0%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 3
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/files/2394D548-668D-49A2-B2AC-2AF77EDD0AAC.jpg?v=1698910548',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 4
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/files/2394D548-668D-49A2-B2AC-2AF77EDD0AAC.jpg?v=1698910548',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 5
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/WhatsAppImage2022-04-04at10.06.13PM_1.jpg?v=1649106251',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 6
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/WhatsAppImage2022-04-04at10.06.15PM.jpg?v=1649106251',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 7
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/WhatsAppImage2022-04-04at10.06.11PM.jpg?v=1649106203',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 8
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/IMG-20230302-WA0002.jpg?v=1677728784',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 9
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/IMG-20230302-WA0003.jpg?v=1677728784',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Image 10
    {
      'type': 'image',
      'track': 1,
      'duration': 3,
      'source': 'https://cdn.shopify.com/s/files/1/0250/7571/2047/products/IMG-20230302-WA0008.jpg?v=1677728784',
      'animations': [
        {
          'type': 'fade',
          'duration': 1,
          'transition': True,
        },
        {
          'type': 'pan',
          'easing': 'linear',
          'scope': 'element',
          'start_x': '0%',
          'start_y': '50%',
          'start_scale': '100%',
          'end_x': '100%',
          'end_y': '50%',
          'end_scale': '120%',
        },
      ],
    },
    # Background music
    {
      'type': 'audio',
      'source': 'https://creatomate-static.s3.amazonaws.com/demo/music1.mp3',
      # Make the audio track as long as the output
      'duration': None,
      # Fade out for 2 seconds
      'audio_fade_out': 2,
    },
  ],
}

response = requests.post(
  'https://api.creatomate.com/v1/renders',
  headers={
    'Authorization': 'Bearer ed4a75900c26407ca57fcae6312b11768e43d6c4be7d41dcd08e30730cb87dace55d5e31ac22d08d7a5483da7d587863',
    'Content-Type': 'application/json',
  },
  json={'source': source}
)
print(response.text)
