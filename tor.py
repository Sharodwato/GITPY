
import numpy as np

# -----------------------------------------
# TORQUE CALCULATOR USING LINEAR REGRESSION
# -----------------------------------------

ITERATIONS = 10

r_data = []
f_data = []

print("=" * 55)
print("  3D PARTICLE TORQUE CALCULATOR")
print("  Regression + Matrix + Cross Product")
print("=" * 55)

# STEP 1: Collect coordinate data
for i in range(ITERATIONS):

    print(f"\n========== ITERATION {i + 1} ==========")

    print("\nEnter position vector r (in metres):")

    rx = float(input("X coordinate: "))
    ry = float(input("Y coordinate: "))
    rz = float(input("Z coordinate: "))

    print("\nEnter force vector F (in Newtons):")

    fx = float(input("X force: "))
    fy = float(input("Y force: "))
    fz = float(input("Z force: "))

    # Store vectors as matrices
    r_vector = np.array([rx, ry, rz])
    f_vector = np.array([fx, fy, fz])

    r_data.append(r_vector)
    f_data.append(f_vector)


# STEP 2: Convert collected data into matrices

R = np.array(r_data)
F = np.array(f_data)

print("\n\nPOSITION MATRIX R:")
print(R)

print("\nFORCE MATRIX F:")
print(F)


# STEP 3: Linear Regression

def regression_estimator(data):

    iterations = np.arange(1, ITERATIONS + 1)

    estimated_vector = []

    for axis in range(3):

        # Fit a linear regression to each component
        slope, intercept = np.polyfit(
            iterations,
            data[:, axis],
            1
        )

        # Estimate component at iteration 10
        predicted_value = (
            slope * ITERATIONS + intercept
        )

        estimated_vector.append(predicted_value)

    return np.array(estimated_vector)


# STEP 4: Estimate position and force vectors

r_estimated = regression_estimator(R)
f_estimated = regression_estimator(F)

print("\n========== REGRESSION RESULTS ==========")

print("\nEstimated Position Vector:")
print(f"r = {r_estimated[0]:.6f}i + "
      f"{r_estimated[1]:.6f}j + "
      f"{r_estimated[2]:.6f}k")

print("\nEstimated Force Vector:")
print(f"F = {f_estimated[0]:.6f}i + "
      f"{f_estimated[1]:.6f}j + "
      f"{f_estimated[2]:.6f}k")


# STEP 5: Convert estimated vectors into matrices

R_final = r_estimated.reshape(3, 1)
F_final = f_estimated.reshape(3, 1)

print("\nFinal Position Matrix:")
print(R_final)

print("\nFinal Force Matrix:")
print(F_final)


# STEP 6: Calculate torque using cross product

torque = np.cross(r_estimated, f_estimated)

print("\n========== TORQUE RESULTS ==========")

print("\nTorque Vector:")

print(
    f"τ = {torque[0]:.6f}i + "
    f"{torque[1]:.6f}j + "
    f"{torque[2]:.6f}k"
)


# STEP 7: Calculate torque magnitude

torque_magnitude = np.linalg.norm(torque)

print("\nTorque Magnitude:")
print(f"|τ| = {torque_magnitude:.6f} N m")


# STEP 8: Display final results

print("\n========== FINAL OUTPUT ==========")

print("Estimated r:", r_estimated)
print("Estimated F:", f_estimated)
print("Torque:", torque)
print("Torque Magnitude:", torque_magnitude)

print("\nCalculation completed successfully.")
