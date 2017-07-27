# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""The afni module provides classes for interfacing with the `AFNI
<http://afni.nimh.nih.gov/afni>`_ command line tools.

Top-level namespace for afni.
"""

from .base import Info
from .preprocess import (AlignEpiAnatPy,Allineate, Automask, 
                         AutoTcorrelate,AutoTLRC,
                         Bandpass, BlurInMask, BlurToFWHM,
                         ClipLevel, DegreeCentrality, Despike,
                         Detrend, ECM, Fim, Fourier, Hist, LFCD,
                         Maskave, Means, OutlierCount,
                         QualityIndex, ROIStats, Retroicor,
                         Seg, SkullStrip, TCorr1D, TCorrMap, TCorrelate,
                         TShift, Volreg, Warp, QwarpPlusMinus, Qwarp)
from .svm import (SVMTest, SVMTrain)
from .utils import (AFNItoNIFTI, Autobox, Axialize, BrickStat, Bucket,
                    Calc, Cat, Copy,
                    Edge3, Eval, FWHMx, MaskTool, Merge, Notes, NwarpApply,
                    Refit, Resample, TCat, TStat, To3D, Unifize, ZCutUp, GCOR,
                    Zcat, Zeropad)
from .model import (Deconvolve, Remlfit)
