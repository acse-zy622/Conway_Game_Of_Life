"""Test automata module functions."""

import os

import numpy as np

import automata

BASE_PATH = os.path.dirname(__file__)


def test_lorenz96():
    """Test Lorenz 96 implementation"""
    initial64 = np.load(os.sep.join((BASE_PATH,
                                     'lorenz96_64_init.npy')))

    onestep64 = np.load(os.sep.join((BASE_PATH,
                                     'lorenz96_64_onestep.npy')))
    assert np.isclose(automata.lorenz96(initial64, 1), onestep64).all()

    thirtystep64 = np.load(os.sep.join((BASE_PATH,
                                        'lorenz96_64_thirtystep.npy')))
    assert np.isclose(automata.lorenz96(initial64, 30), thirtystep64).all()
