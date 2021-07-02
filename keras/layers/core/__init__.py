# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Core Keras layers."""

from keras.layers.core.activation import Activation
from keras.layers.core.activity_regularization import ActivityRegularization
from keras.layers.core.class_method import ClassMethod
from keras.layers.core.dense import Dense
from keras.layers.core.dropout import Dropout
from keras.layers.core.flatten import Flatten
from keras.layers.core.instance_method import InstanceMethod
from keras.layers.core.instance_property import InstanceProperty
from keras.layers.core.keras_op_dispatcher import KerasOpDispatcher
from keras.layers.core.lambda_layer import Lambda
from keras.layers.core.masking import Masking
from keras.layers.core.permute import Permute
import keras.layers.core.ragged_patches
from keras.layers.core.ragged_patches import ragged_class_method
from keras.layers.core.repeat_vector import RepeatVector
from keras.layers.core.reshape import Reshape
from keras.layers.core.slicing_ops import SlicingOpLambda
from keras.layers.core.slicing_ops import TFSlicingOpDispatcher
import keras.layers.core.sparse_patches
from keras.layers.core.spatial_dropout_1d import SpatialDropout1D
from keras.layers.core.spatial_dropout_2d import SpatialDropout2D
from keras.layers.core.spatial_dropout_3d import SpatialDropout3D
from keras.layers.core.tf_op_lambda import TFOpLambda
