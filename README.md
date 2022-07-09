
# Satellite Geodesy Perifocal Coordinate Transformation

## Statement

**Step by step how the calculations are made is given in the .pfd file**. Excel functions are in Turkish. Randomly generated coordinates were created based on the school numbers of the students. According to your student number, true anomaly ($v^◦$), satellite orbit major semi-axis ($a$), and satellite orbit eccentricity ($e$) were produced. According to these data, the perifocal ($P, Q, W$) coordinates of the satellite were calculated. Then, inclination angle ($İ^◦$), recitation angle ($Ω^◦$), and perigee argument ($ω^◦$) will be produced according to your student number. Calculate the Earth-centered Inertial (ECI) coordinates from the $PQW$ coordinates of the point you obtained from previous section.

<br>

### Calculation coordinates of  $P, Q ,W$

The values ​​corresponding to my number in the project are given below. Perifocal coordinates have been calculated by taking the values ​​of a value in meters and kilometers as reference. Since the calculations are in 2 dimensional plane, omega value is taken as 0. Calculations are made in units of kilometers.

**True anomaly:**

$v^◦ = 153^◦. 620668966$  

**Satellite orbit major half-axis:**

$a = 9131.00835200 \medspace m$

**Satellite orbital axiality:**

$e = 7.704$



We can calculate $P, Q ,W$ coordinates with following equation.

$$r(PQW) =\dfrac{a (1 - e^2)}{1 + e * \cos(v)} \medspace * \medspace\begin{matrix*}[r]  
cos(v) \\  
sin(v) \\
0
\end{matrix*}$$

Differential equation of orbit: 

$$\dfrac{a (1 - e^2)}{1 + e * \cos(v)}$$

Results have shown below:

$P = -80.8821594551 \medspace km$
$Q = 40.1138553510 \medspace km$
$W = 0 \medspace km$

<br>

### Calculation coordinates of ECI

The ECI coordinate system is a fixed inertial coordinate system with respect to the stars. ECI being fixed with respect to the stars means that it does not rotate with the earth (non-rotating). The values ​​corresponding to my number in the project are given below.

**Angle of inclination:**
$$İ^◦ = 58^◦. 32222222$$
**Angle of rectification:**
$$Ω^◦ = 5^◦.45$$
**Perigee argument:**
$$ω^◦ = 268^◦.9310345$$

<br>

**Rotation matrices:** 

$$R_x(\theta) = \begin{vmatrix*}[r]  
1 & 0 & 0\\
0 & cos\theta & -sin\theta\\  
0 & sin\theta  & cos\theta
\end{vmatrix*}$$

    R1x = np.array([[1, 0, 0],
                   [0, m.cos(m.radians(-a)), m.sin(m.radians(-a))],
                   [0, -m.sin(m.radians(-a)), m.cos(m.radians(-a))]])

$$R_y(\theta) = \begin{vmatrix*}[r]  
cos\theta & 0 & sin\theta\\
0 & 1 & 0\\  
-sin\theta & 0  & cos\theta
\end{vmatrix*}$$

    R3y = np.array([[m.cos(m.radians(-a)), 0, m.sin(m.radians(-a))],
                   [0, 1, 0],
                   [-m.sin(m.radians(-a)), 0, m.cos(m.radians(-a))]])

$$R_z(\theta) = \begin{vmatrix*}[r]  
cos\theta & -sin\theta & 0\\
sin\theta & cos\theta & 0\\  
0 & 0  & 1
\end{vmatrix*}$$

    R3z = np.array([[m.cos(m.radians(-a)), m.sin(m.radians(-a)), 0],
                   [-m.sin(m.radians(-a)), m.cos(m.radians(-a)), 0],
                   [0, 0, 1]])

<br>

To calculate rECI, we need to make matrix multiplication using our rotation matrices.

$rECI = R_z(-\Omega) ⋅ R_x(-i) ⋅ R_z(-\omega) ⋅ rPQW$

    R1ixR3w = np.matmul(R1i, R3w)
    R3wR1R3 = np.matmul(R3omega, R1ixR3w)
    ECI = np.matmul(R3wR1R3, PQW)

<br>

ECI coordinates have shown below:

$$rECI = \medspace\begin{matrix*}[r]  
37.43159216 \\  
45.83655056 \\
68.18307452
\end{matrix*}$$

## How to Run Code

Before running the code make sure that you have these libraries:

 - math 
 - numpy 


## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak)  
 - Mail address: doguilmak@gmail.com
