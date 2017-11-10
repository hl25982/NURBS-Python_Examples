# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a BSpline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up the NURBS curve
curve.read_ctrlpts_from_txt("ex_curve03.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts03_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts03_orig.csv")

# Evaluate curve tangent at u = 0.0
curvetan1 = curve.tangent(0.0, normalize=True)

# Evaluate curve tangent at u = 0.2
curvetan2 = curve.tangent(0.2, normalize=True)

# Evaluate curve tangent at u = 0.5
curvetan3 = curve.tangent(0.5, normalize=True)

# Evaluate curve tangent at u = 0.6
curvetan4 = curve.tangent(0.6, normalize=True)

# Evaluate curve tangent at u = 0.8
curvetan5 = curve.tangent(0.8, normalize=True)

# Evaluate curve tangent at u = 1.0
curvetan6 = curve.tangent(1.0, normalize=True)

# Good to have something here to put a breakpoint
pass