#!/bin/bash
currdate=`date +%Y%m%d-%H`
echo ${currdate}

source activate pytorch-CycleGAN-and-pix2pix

#nohup \
python train.py \
	--dataroot ./datasets/vspRaw \
	--name vsp_raw_20180807 \
	--model pix2pix \
	--which_model_netG unet_256 \
	--which_direction BtoA \
	--dataset_mode rawdata \
	--no_lsgan \
	--norm batch \
	--gpu_ids -1 \
	--pool_size 0 \
	--output_nc 2 \
	--input_nc 2 \
	--niter 10 \
	--display_freq 50 \
	--save_epoch_freq 50 \
	--save_latest_freq 100 \
	--no_flip \
	--no_dropout \
	> out_vspRaw_train${currdate}.log #2>&1 &

echo "Training begin..."

	#--gpu_ids 1 \
	#--name vsp_test_01_20180804 \
	#--model pix2pix \
	#--lambda_A 100 \
	#--display_server http://172.16.31.160 \
#echo "Begin Visualizer..."
#python -m visdom.server

exit 0

