# noise_reduction_through_image_fusion
A computational photography technique combines multiple image exposures to recovers lost color and detail without injecting editing preferences. The project leverages OpenCV, Scikit, and numpy to expedite computations and reduce complexity. Please see included PDF file for research paper.

## Comments
- To run the program ensure you have two subdirectories: one named input, and another named output.
- The program will take 2-image sets where the first image is evenly exposed and the second image is brighter.
- The program will batch process as many images as are contained in the image folder. They must be sequential pairs.
- The program will output all steps of the algorithm. To use this for general purpose processing, it will be neccesary to comment out
  unneeded output lines in the python file.
- The output files currently here for example output can be deleted for a fresh run.


The images included are from Googles HDR+ Burst Photography Dataset used in the following research: @article{hasinoff2016burst, author = {Samuel W. Hasinoff and Dillon Sharletand Ryan Geiss and Andrew Adams and Jonathan T. Barron and Florian Kainz and Jiawen Chen and Marc Levoy}, title = {Burst photography for high dynamic range and low-light imaging on mobile cameras}, journal = {ACM Transactions on Graphics (Proc. SIGGRAPH Asia)}, volume = {35}, number = {6}, year = {2016}, }               


Creator: Ryan Filgas
