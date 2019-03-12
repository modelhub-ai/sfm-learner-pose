# sfm-learner-pose
This repository hosts the contributor source files for the sfm-learner-pose model. ModelHub integrates these files into an engine and controlled runtime environment. A unified API allows for out-of-the-box reproducible implementations of published models. For more information, please visit [www.modelhub.ai](http://modelhub.ai/) or contact us [info@modelhub.ai](mailto:info@modelhub.ai).
## meta
| | |
|-|-|
| id | ce585219-d617-4864-b225-06b52532ea95 | 
| application_area | Capsule Endoscopy | 
| task | Pose & Depth Estimation | 
| task_extended | Unsupervised Pose & Depth Estimation | 
| data_type | Image/Photo | 
| data_source | http://www.cvlibs.net/datasets/kitti/ | 
## publication
| | |
|-|-|
| title | Unsupervised Odometry and Depth Learning for Endoscopic Capsule Robots | 
| source | arxiv | 
| url | https://arxiv.org/abs/1803.01047 | 
| year | 2018 | 
| authors | Turan Mehmet, Ornek E. Pinar, Ibrahimli Nail, Giracoglu Can, Almalioglu Yasin, Yanik M. Fatih, Sitti Metin | 
| abstract | In the last decade, many medical companies and research groups have tried to convert passive capsule endoscopes as an emerging and minimally invasive diagnostic technology into actively steerable endoscopic capsule robots which will provide more intuitive disease detection, targeted drug delivery and biopsy-like operations in the gastrointestinal(GI) tract. In this study, we introduce a fully unsupervised, real-time odometry and depth learner for monocular endoscopic capsule robots. We establish the supervision by warping view sequences and assigning the re-projection minimization to the loss function, which we adopt in multi-view pose estimation and single-view depth estimation network. Detailed quantitative and qualitative analyses of the proposed framework performed on non-rigidly deformable ex-vivo porcine stomach datasets proves the effectiveness of the method in terms of motion estimation and depth recovery. | 
| google_scholar | https://scholar.google.com/scholar?oi=bibs&hl=en&cites=16480963845558763827&as_sdt=5 | 
| bibtex | @ARTICLE{2018arXiv180301047T, author = {{Turan}, Mehmet and {Pinar Ornek}, Evin and {Ibrahimli}, Nail and {Giracoglu}, Can and {Almalioglu}, Yasin and {Yanik}, Mehmet Fatih and {Sitti}, Metin}, title = {Unsupervised Odometry and Depth Learning for Endoscopic Capsule Robots}, journal = {arXiv e-prints}, keywords = {Computer Science - Robotics}, year = 2018, month = Mar, eid = {arXiv:1803.01047}, pages = {arXiv:1803.01047}, archivePrefix = {arXiv}, eprint = {1803.01047}, primaryClass = {cs.RO}} | 
## model
| | |
|-|-|
| description | The model consists of two networks trained together, first one being single-view depth network and the second one pose-reliability network. Both of them have decoder-encoder design, a stack of convolutional networks. | 
| provenance | contributed by author |
| architecture | Convolutional Neural Network(CNN), Decoder/Encoder | 
| learning_type | Unsupervised learning | 
| format | .pb | 
| I/O | model I/O can be viewed [here](contrib_src/model/config.json) | 
| license | model license can be viewed [here](contrib_src/license/model) | 
## run
To run this model and view others in the collection, view the instructions on [ModelHub](http://app.modelhub.ai/).
## contribute
To contribute models, visit the [ModelHub docs](https://modelhub.readthedocs.io/en/latest/).

