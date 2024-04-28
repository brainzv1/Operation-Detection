import os


dataset_type = 'VideoDataset'
project_path = os.getcwd()
train_dir = os.path.join(project_path, "mmaction2", "DataSet", "train")
test_dir = os.path.join(project_path, "mmaction2", "DataSet", "test") #Still need change for this to work
val_dir = os.path.join(project_path, "mmaction2", "DataSet", "val")

_base_ = [
    os.path.join(os.getcwd(), "mmaction2", "configs", "_base_", "models", "tsn_r50.py"),
    os.path.join(os.getcwd(), "mmaction2", "configs", "_base_", "schedules", "sgd_100e.py"),
    os.path.join(os.getcwd(), "mmaction2", "configs", "_base_", "default_runtime.py")
]

data_set_dir = os.path.join(project_path, "mmaction2", "DataSet")
# Construct file paths
ann_file_train = os.path.join(data_set_dir, "train.txt")
ann_file_val = os.path.join(data_set_dir, "val.txt")
ann_file_test = os.path.join(data_set_dir, "test.txt")

data_root = train_dir
data_root_val = val_dir
data_root_test = test_dir

file_client_args = dict(io_backend='disk')

train_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(type='SampleFrames', clip_len=1, frame_interval=1, num_clips=3),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(
        type='MultiScaleCrop',
        input_size=224,
        scales=(1, 0.875, 0.75, 0.66),
        random_crop=False,
        max_wh_scale_gap=1),
    dict(type='Resize', scale=(224, 224), keep_ratio=False),
    dict(type='Flip', flip_ratio=0.5),
    dict(type='FormatShape', input_format='NCHW'),
    dict(type='PackActionInputs')
]
val_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(
        type='SampleFrames',
        clip_len=1,
        frame_interval=1,
        num_clips=3,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCHW'),
    dict(type='PackActionInputs')
]
test_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(
        type='SampleFrames',
        clip_len=1,
        frame_interval=1,
        num_clips=25,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='TenCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCHW'),
    dict(type='PackActionInputs')
]

train_dataloader = dict(
    batch_size=32,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_train,
        data_prefix=dict(video=data_root),
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=16,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_val,
        data_prefix=dict(video=data_root_val),
        pipeline=val_pipeline,
        test_mode=True))
test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_test,
        data_prefix=dict(video=data_root_test),
        pipeline=test_pipeline,
        test_mode=True))

val_evaluator = dict(type='AccMetric')
test_evaluator = val_evaluator

default_hooks = dict(checkpoint=dict(interval=3, max_keep_ckpts=3))

# Default setting for scaling LR automatically
#   - `enable` means enable scaling LR automatically
#       or not by default.
#   - `base_batch_size` = (8 GPUs) x (32 samples per GPU).
auto_scale_lr = dict(enable=False, base_batch_size=256)


# default_scope = 'mmaction'  # The default registry scope to find modules. Refer to https://mmengine.readthedocs.io/en/latest/tutorials/registry.html
# default_hooks = dict(  # Hooks to execute default actions like updating model parameters and saving checkpoints.
#     runtime_info=dict(type='RuntimeInfoHook'),  # The hook to updates runtime information into message hub
#     timer=dict(type='IterTimerHook'),  # The logger used to record time spent during iteration
#     logger=dict(
#         type='LoggerHook',  # The logger used to record logs during training/validation/testing phase
#         interval=20,  # Interval to print the log
#         ignore_last=False), # Ignore the log of last iterations in each epoch
#     param_scheduler=dict(type='ParamSchedulerHook'),  # The hook to update some hyper-parameters in optimizer
#     checkpoint=dict(
#         type='CheckpointHook',  # The hook to save checkpoints periodically
#         interval=3,  # The saving period
#         save_best='auto',  # Specified metric to mearsure the best checkpoint during evaluation
#         max_keep_ckpts=3),  # The maximum checkpoints to keep
#     sampler_seed=dict(type='DistSamplerSeedHook'),  # Data-loading sampler for distributed training
#     sync_buffers=dict(type='SyncBuffersHook'))  # Synchronize model buffers at the end of each epoch
# env_cfg = dict(  # Dict for setting environment
#     cudnn_benchmark=False,  # Whether to enable cudnn benchmark
#     mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0), # Parameters to setup multiprocessing
#     dist_cfg=dict(backend='nccl')) # Parameters to setup distributed environment, the port can also be set
#
# log_processor = dict(
#     type='LogProcessor',  # Log processor used to format log information
#     window_size=20,  # Default smooth interval
#     by_epoch=True)  # Whether to format logs with epoch type
# vis_backends = [  # List of visualization backends
#     dict(type='LocalVisBackend')]  # Local visualization backend
# visualizer = dict(  # Config of visualizer
#     type='ActionVisualizer',  # Name of visualizer
#     vis_backends=vis_backends)
# log_level = 'INFO'  # The level of logging
# load_from = None  # Load model checkpoint as a pre-trained model from a given path. This will not resume training.
# resume = False  # Whether to resume from the checkpoint defined in `load_from`. If `load_from` is None, it will resume the latest checkpoint in the `work_dir`.
# ...

