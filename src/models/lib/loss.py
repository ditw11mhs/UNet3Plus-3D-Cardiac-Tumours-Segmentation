"""Module for log cosh loss"""
import keras.backend as K
import tensorflow as tf


def generalized_dice_coefficient_basic( y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection=K.sum(y_true_f * y_pred_f, axis=-1)
    denom = K.sum(y_true_f + y_pred_f, axis=-1)
    score = (2. * intersection + smooth) / (denom + smooth)
    return score

def generalized_dice_coefficient(y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true[...,1:])
    y_pred_f = K.flatten(y_pred[...,1:])
    intersection=K.sum(y_true_f * y_pred_f)
    denom = K.sum(y_true_f + y_pred_f)

    score = K.mean((2. * intersection) / (denom + smooth))
    return score

def dice_loss( y_true, y_pred):
    loss = 1 - generalized_dice_coefficient(y_true, y_pred)
    return loss
    
def log_cosh_dice_loss_func( y_true, y_pred):
    """
    An implementation of log cosh loss based on
    'A survey of loss functions for semantic segmentation'
    by Shruti Jadon

    Loss implementation based on
    https://github.com/shruti-jadon/Semantic-Segmentation-Loss-Functions
    Survey Paper DOI: 10.1109/CIBCB48159.2020.9277638

    Args:
        y_true ():
        y_pred ():

    Returns:

    """
    x = dice_loss(y_true, y_pred)
    return tf.math.log((tf.exp(x) + tf.exp(-x)) / 2.0)
