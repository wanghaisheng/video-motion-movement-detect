'''
Copyright 2021 D3M Team
Copyright (c) 2021 DATA Lab at Texas A&M University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from d3m import container
from d3m.metadata import hyperparams
import imgaug.augmenters as iaa

from autovideo.utils import construct_primitive_metadata
from autovideo.base.augmentation_base import AugmentationPrimitiveBase

__all__ = ('ReplaceElementwisePrimitive',)

Inputs = container.DataFrame

class Hyperparams(hyperparams.Hyperparams):
    replacement = hyperparams.List[int](
        default=[0,255],
        description=' The size of the lower resolution image from which to sample the replacement mask in percent of the input image. ',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )
    seed = hyperparams.Constant[int](
        default=0,
        description='Minimum workers to extract frames simultaneously',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )
    mask = hyperparams.Constant[float](
        default=0.1,
        description='The probability of an image to be inverted.',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )


class ReplaceElementwisePrimitive(AugmentationPrimitiveBase[Inputs, Hyperparams]):
    """
    A primitive which Replace rectangular areas in images with white-ish pixel noise.
    """

    metadata = construct_primitive_metadata("augmentation", "arithmetic_ReplaceElementwise")

    def _get_function(self):
        """
        set up function and parameter of functions
        """
        seed = self.hyperparams["seed"]
        mask = self.hyperparams["mask"]
        replacement = self.hyperparams["replacement"]
        return iaa.ReplaceElementwise(mask=mask,replacement=replacement,seed=seed)