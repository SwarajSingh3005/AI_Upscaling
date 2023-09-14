Abstract

AI image upscaling uses artificial intelligence algorithms to improve the resolution of an image. 

Nowadays, most people own a 4k TV in their home that can display ultra-HD content. However, when watching lower-resolution content, the video must be upscaled to fill out the entire display. 1080p images, known as full HD, have just a quarter of the pixels in 4K images. The picture has to be stretched to match the TV's pixels to display a 1080p shot from edge to edge on a 4K screen. In this situation, we use AI upscaling to improve the image quality of low image/video content.

Detailed Description

In the technique, "AI upscaling", the application,when fed with a low-resolution image, will generate a similar idea with more
pixels. It is achieved in two ways. One, by filling the additional pixels with similar visual information – also called nearest neighbour resizing. Two,creating interstitial pixels to smooth the transition between pixels with low-resolution pixels. The algorithms make a seamless image in both methods by recognising
common contrast patterns in real-world scenarios. 

"Generally, these image synthesis tasks are performed by deep generative models, such as GANs, VAEs, and autoregressive models. Nevertheless, each of these generative models has its downsides when trained to synthesise high-quality samples on difficult, high resolution datasets. For example, GANs often suffer from unstable training and mode collapse, and autoregressive models typically suffer from slow synthesis speed." (Jonathan Ho,2021)

There are many real-world problems, like restoring vintage old low-resolution photos into high-resolution photos or upscaling a video for a bigger-resolution screen; doing all these manually would take much time and human resources. So, in this case, and many other issues, we should use AI upscaling because it saves money, the results are more accurate, and it improves image resolution instantly.


Data set

The dataset is commonly used for training and evaluation of the image-super-resolution task. DIV2K dataset has 1000 2K resolution images divided into 800 images for training, 100 images for validation, 100 images for testing, which is a large diversity of contents.

https://data.vision.ee.ethz.ch/cvl/DIV2K/


Architecture Proposal

This paper discusses how we can restore old photos using the DIV2K dataset. It is designed to repair defects, such as scratches and dust spots, and a local department targeting unstructured defects, such as noises and blurriness.

Zi-Yu Wan, Bo Zhang, Dong-Dong Chen, Pan Zhang, Dong Chen, Jing Liao, Fang Wen.Bringing Old Photos Back to Life, https://paperswithcode.com/paper/bringing-old-photos-back-to-life




This article summarises the existing super-resolution techniques into three categories which are supervised, unsupervised, and domain specific. It also talks about publicly available benchmark datasets and performance evaluation metrics.

Wang, Zhihao, et al. Deep Learning for Image Super-Resolution: A Survey. arXiv, 7 Feb. 2020. arXiv.org, https://doi.org/10.48550/arXiv.1902.06068.



![Screenshot-1056-800x310](https://user-images.githubusercontent.com/114939556/202602258-c25f8eca-1210-4272-ad81-ceb959c0365b.jpg)

This image showing AI upscaling, A 32×32 photo can be enhanced to 64×64 and then 256×256.(Zhang,2021)


![cascadibng-800x375](https://user-images.githubusercontent.com/114939556/202602507-75d89f1f-25eb-4527-83a1-caec4ed4060a.jpg)

This image showing AI upscaling, A 64×64 photo can be upscaled to 256×256 and then 1024×1024(Zhang,2021)



Reference 

Jonathan Ho,(2021). High-Fidelity Image Generation Using Diffusion Models https://ai.googleblog.com/2021/07/high-fidelity-image-generation-using.html?m=1

MICHAEL ZHANG, 2021, Google’s New AI Photo Upscaling Tech is Jaw-Dropping, < https://petapixel.com/assets/uploads/2021/08/cascadibng-800x375.jpg >.

MICHAEL ZHANG, 2021, Google’s New AI Photo Upscaling Tech is Jaw-Dropping, < https://petapixel.com/assets/uploads/2021/08/Screenshot-1056-800x310.jpg >.
