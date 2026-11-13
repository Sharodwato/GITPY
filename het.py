
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor


# =====================================================
# 3D PARTICLE TORQUE CALCULATOR
# AI REGRESSION + ANGLE MEASUREMENTS + CROSS PRODUCT
# =====================================================

ITERATIONS = 5
PREDICTION_ITERATION = 9

# -----------------------------------------------------
# INPUT VALIDATION
# -----------------------------------------------------

def get_number(message):

    while True:
        try:
            value = float(input(message))

            if not np.isfinite(value):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a numerical value.")


def get_vector(name, unit):

    print(f"\nEnter {name} vector ({unit}):")

    x = get_number("X component: ")
    y = get_number("Y component: ")
    z = get_number("Z component: ")

    return np.array([x, y, z], dtype=float)


def calculate_angle(r, f):

    r_mag = np.linalg.norm(r)
    f_mag = np.linalg.norm(f)

    if r_mag == 0 or f_mag == 0:
        return None

    cosine = np.dot(r, f) / (r_mag * f_mag)

    cosine = np.clip(cosine, -1.0, 1.0)

    angle = np.degrees(np.arccos(cosine))

    return angle


# -----------------------------------------------------
# STEP 1: COLLECT 10 OBSERVATIONS
# -----------------------------------------------------

R_data = []
F_data = []
angle_data = []

print("=" * 60)
print("       AI PARTICLE TORQUE CALCULATOR")
print("       RANDOM FOREST REGRESSION")
print("=" * 60)

for i in range(ITERATIONS):

    print(f"\n========== ITERATION {i + 1} ==========")

    # Position vector
    r = get_vector("Position r", "metres")

    # Force vector
    f = get_vector("Force F", "Newtons")

    # Angle between position and force
    print("\nEnter the angle between r and F:")

    angle = get_number("Angle (degrees): ")

    while not 0 <= angle <= 180:
        print("Angle must be between 0 and 180 degrees.")
        angle = get_number("Enter angle again: ")

    # Calculate angle independently
    calculated_angle = calculate_angle(r, f)

    if calculated_angle is not None:

        print(
            f"Geometrically calculated angle: "
            f"{calculated_angle:.4f} degrees"
        )

        if abs(angle - calculated_angle) > 2:
            print("WARNING: Input angle and vector angle differ.")
            print("Please verify your measurements.")

    else:
        print("WARNING: Angle cannot be verified for a zero vector.")

    R_data.append(r)
    F_data.append(f)
    angle_data.append(angle)


# -----------------------------------------------------
# STEP 2: CONVERT DATA INTO MATRICES
# -----------------------------------------------------

R = np.array(R_data)
F = np.array(F_data)
Angles = np.array(angle_data)

print("\n========== INPUT MATRICES ==========")

print("\nPosition Matrix R:")
print(R)

print("\nForce Matrix F:")
print(F)

print("\nAngle Matrix:")
print(Angles.reshape(-1, 1))


# -----------------------------------------------------
# STEP 3: PREPARE MACHINE LEARNING DATA
# -----------------------------------------------------

# Independent variable: iteration number
X = np.arange(1, ITERATIONS + 1).reshape(-1, 1)

# Combine all seven dependent variables:
# rx, ry, rz, fx, fy, fz, angle

Y = np.column_stack((
    R,
    F,
    Angles
))


# -----------------------------------------------------
# STEP 4: TRAIN RANDOM FOREST AI REGRESSION
# -----------------------------------------------------

print("\n========== AI MODEL TRAINING ==========")

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=4,
    random_state=42,
    min_samples_leaf=1
)

model.fit(X, Y)

print("Random Forest model trained successfully.")

# Predict 11th iteration
X_next = np.array([[PREDICTION_ITERATION]])

ai_prediction = model.predict(X_next)[0]

# Separate predicted variables
r_predicted = ai_prediction[0:3]
f_predicted = ai_prediction[3:6]
angle_predicted = np.clip(
    ai_prediction[6], 0, 180
)


# -----------------------------------------------------
# STEP 5: AI-ESTIMATED AVERAGE
# -----------------------------------------------------

# Predictions of the trained model across
# the original ten iterations

fitted_predictions = model.predict(X)

ai_average = np.mean(fitted_predictions, axis=0)

r_ai_average = ai_average[0:3]
f_ai_average = ai_average[3:6]
angle_ai_average = np.clip(
    ai_average[6], 0, 180
)

# Actual measurement averages for comparison
r_observed_average = np.mean(R, axis=0)
f_observed_average = np.mean(F, axis=0)
angle_observed_average = np.mean(Angles)


# -----------------------------------------------------
# STEP 6: DISPLAY AI PREDICTIONS
# -----------------------------------------------------

def display_vector(name, vector, unit):

    print(f"\n{name}:")

    print(
        f"{vector[0]:.6f} i + "
        f"{vector[1]:.6f} j + "
        f"{vector[2]:.6f} k {unit}"
    )


print("\n========== 11TH ITERATION PREDICTION ==========")

display_vector(
    "Predicted Position Vector",
    r_predicted,
    "m"
)

display_vector(
    "Predicted Force Vector",
    f_predicted,
    "N"
)

print(f"\nPredicted Angle: {angle_predicted:.6f} degrees")


print("\n========== AI-ESTIMATED AVERAGE ==========")

display_vector(
    "AI Average Position",
    r_ai_average,
    "m"
)

display_vector(
    "AI Average Force",
    f_ai_average,
    "N"
)

print(f"\nAI Average Angle: {angle_ai_average:.6f} degrees")


print("\n========== OBSERVED DATA AVERAGES ==========")

display_vector(
    "Observed Average Position",
    r_observed_average,
    "m"
)

display_vector(
    "Observed Average Force",
    f_observed_average,
    "N"
)

print(
    f"\nObserved Average Angle: "
    f"{angle_observed_average:.6f} degrees"
)


# -----------------------------------------------------
# STEP 7: CALCULATE TORQUE
# -----------------------------------------------------

# Torque = r x F

torque_11 = np.cross(
    r_predicted,
    f_predicted
)

torque_ai_average = np.cross(
    r_ai_average,
    f_ai_average
)

# Calculate torque for every original observation

torque_observed = np.cross(R, F)

# Average of the individual observed torques
mean_observed_torque = np.mean(
    torque_observed,
    axis=0
)


# -----------------------------------------------------
# STEP 8: TORQUE MAGNITUDE
# -----------------------------------------------------

magnitude_11 = np.linalg.norm(torque_11)

magnitude_ai_average = np.linalg.norm(
    torque_ai_average
)

mean_observed_magnitude = np.mean(
    np.linalg.norm(torque_observed, axis=1)
)


# -----------------------------------------------------
# STEP 9: DISPLAY FINAL TORQUE
# -----------------------------------------------------

print("\n========== FINAL TORQUE RESULTS ==========")

display_vector(
    "11th Iteration Torque",
    torque_11,
    "N m"
)

print(
    f"11th Iteration Torque Magnitude: "
    f"{magnitude_11:.8f} N m"
)

display_vector(
    "AI Average Torque",
    torque_ai_average,
    "N m"
)

print(
    f"AI Average Torque Magnitude: "
    f"{magnitude_ai_average:.8f} N m"
)

display_vector(
    "Mean Observed Torque",
    mean_observed_torque,
    "N m"
)

print(
    f"Mean Observed Torque Magnitude: "
    f"{mean_observed_magnitude:.8f} N m"
)


# -----------------------------------------------------
# STEP 10: PHYSICAL CONSISTENCY CHECK
# -----------------------------------------------------

print("\n========== ANGLE CONSISTENCY CHECK ==========")

geometric_11 = calculate_angle(
    r_predicted,
    f_predicted
)

geometric_average = calculate_angle(
    r_ai_average,
    f_ai_average
)

if geometric_11 is not None:

    print(
        f"AI predicted angle: "
        f"{angle_predicted:.4f} degrees"
    )

    print(
        f"Angle from predicted vectors: "
        f"{geometric_11:.4f} degrees"
    )

    print(
        "Predicted angle difference: "
        f"{abs(angle_predicted - geometric_11):.4f} degrees"
    )

if geometric_average is not None:

    print(
        f"\nAI average angle: "
        f"{angle_ai_average:.4f} degrees"
    )

    print(
        f"Angle from AI average vectors: "
        f"{geometric_average:.4f} degrees"
    )


# -----------------------------------------------------
# STEP 11: VISUALIZATION
# -----------------------------------------------------

iterations = np.arange(1, ITERATIONS + 1)

# Plot 1: Regression and torque results

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Position regression
for i, label in enumerate(["Rx", "Ry", "Rz"]):

    axes[0, 0].plot(
        iterations, R[:, i],
        marker="o", label=label
    )

    axes[0, 0].scatter(
        11, r_predicted[i],
        marker="X", s=100
    )

axes[0, 0].set_title("Position Vector Regression")
axes[0, 0].set_xlabel("Iteration")
axes[0, 0].set_ylabel("Position (m)")
axes[0, 0].legend()
axes[0, 0].grid(True)

# Force regression
for i, label in enumerate(["Fx", "Fy", "Fz"]):

    axes[0, 1].plot(
        iterations, F[:, i],
        marker="o", label=label
    )

    axes[0, 1].scatter(
        11, f_predicted[i],
        marker="X", s=100
    )

axes[0, 1].set_title("Force Vector Regression")
axes[0, 1].set_xlabel("Iteration")
axes[0, 1].set_ylabel("Force (N)")
axes[0, 1].legend()
axes[0, 1].grid(True)

# Angle regression
axes[1, 0].plot(
    iterations,
    Angles,
    marker="o",
    label="Measured angle"
)

axes[1, 0].scatter(
    11,
    angle_predicted,
    marker="X",
    s=100,
    label="AI prediction"
)

axes[1, 0].set_title("Angle Regression")
axes[1, 0].set_xlabel("Iteration")
axes[1, 0].set_ylabel("Angle (degrees)")
axes[1, 0].legend()
axes[1, 0].grid(True)

# Torque magnitude
observed_magnitudes = np.linalg.norm(
    torque_observed,
    axis=1
)

axes[1, 1].plot(
    iterations,
    observed_magnitudes,
    marker="o",
    label="Observed torque"
)

axes[1, 1].scatter(
    11,
    magnitude_11,
    marker="X",
    s=100,
    label="Predicted torque"
)

axes[1, 1].set_title("Torque Magnitude")
axes[1, 1].set_xlabel("Iteration")
axes[1, 1].set_ylabel("Torque (N m)")
axes[1, 1].legend()
axes[1, 1].grid(True)

plt.tight_layout()

plt.savefig(
    "torque_regression_results.png",
    dpi=300
)

plt.show()


# -----------------------------------------------------
# STEP 12: 3D VECTOR VISUALIZATION
# -----------------------------------------------------

fig = plt.figure(figsize=(12, 6))

# Position vectors
ax1 = fig.add_subplot(121, projection="3d")

ax1.quiver(
    0, 0, 0,
    *r_predicted,
    color="red",
    label="11th iteration"
)

ax1.quiver(
    0, 0, 0,
    *r_ai_average,
    color="blue",
    label="AI average"
)

ax1.set_title("Estimated Position Vectors")
ax1.set_xlabel("X (m)")
ax1.set_ylabel("Y (m)")
ax1.set_zlabel("Z (m)")
ax1.legend()

# Force vectors
ax2 = fig.add_subplot(122, projection="3d")

ax2.quiver(
    0, 0, 0,
    *f_predicted,
    color="red",
    label="11th iteration"
)

ax2.quiver(
    0, 0, 0,
    *f_ai_average,
    color="blue",
    label="AI average"
)

ax2.set_title("Estimated Force Vectors")
ax2.set_xlabel("X (N)")
ax2.set_ylabel("Y (N)")
ax2.set_zlabel("Z (N)")
ax2.legend()

plt.tight_layout()

plt.savefig(
    "particle_vectors_3D.png",
    dpi=300
)

plt.show()


# -----------------------------------------------------
# COMPLETION
# -----------------------------------------------------

print("\n" + "=" * 60)
print("          CALCULATION COMPLETED")
print("=" * 60)

print("\nGenerated files:")
print("1. torque_regression_results.png")
print("2. particle_vectors_3D.png")
