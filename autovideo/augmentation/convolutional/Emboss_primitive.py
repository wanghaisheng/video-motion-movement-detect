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

__all__ = ('EmbossPrimitive',)

Inputs = container.DataFrame

class Hyperparams(hyperparams.Hyperparams):

    alpha = hyperparams.Set[float](
        default=(0.0, 1.0),
        description="Blending factor of the sharpened image. At 0.0, only the original image is visible, at 1.0 only its sharpened version is visible",
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )

    strength = hyperparams.Set[float](
        default=(0.5, 1.5),
        description="Parameter that controls the strength of the embossing. Sane values are somewhere in the interval [0.0, 2.0] with 1.0 being the standard embossing effect. Default value is 1.0.",
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )

    seed = hyperparams.Constant[int](
        default=0,
        description='Minimum workers to extract frames simultaneously',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
    )



class EmbossPrimitive(AugmentationPrimitiveBase[Inputs, Hyperparams]):
    """
    A primitive which Augmenter that embosses images and overlays the result with the original image.
    """

    metadata = construct_primitive_metadata("augmentation", "convolutional_Emboss")

    def _get_function(self):
        """
        set up function and parameter of functions
        """
        alpha = self.hyperparams["alpha"]
        strength = self.hyperparams["strength"]
        seed = self.hyperparams["seed"]
        return iaa.Emboss(alpha=alpha, strength=strength, seed=seed)
