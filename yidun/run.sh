if [ $1 = "yolo_valid" ] ; then
../darknet detector valid config/captcha.data config/yolov3-captcha.cfg checkpoints/yolov3-captcha_final.weights

elif [ $1 = "yolo_train" ] ; then
../darknet detector train config/captcha.data config/yolov3-captcha.cfg ../weights/darknet53.conv.74

elif [ $1 = "classifier_train" ] ; then
../darknet classifier train config/chinese_classify.data config/chinese_classify.cfg

elif [ $1 = "classifier_valid" ] ; then
./darknet classifier valid config/chinese_classify.data config/chinese_classify.cfg classify_checkpoints/chinese_character.weights


