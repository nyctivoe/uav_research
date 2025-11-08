# Definitions

**State Space** -> $[x, y, z, v_x, v_y, v_z, pitch, roll, yaw, \omega_x, \omega_y, \omega_z, wind_x, wind_y, wind_z]$
**Sction Space** -> $[\Delta\omega_1, \Delta\omega_2, \Delta\omega_3, \Delta\omega_4]$

**Reward Function** -> $R = \alpha R_1 + \beta R_2 + \gamma R_3 + \delta R_4 + \epsilon R_5$

where: 

- $R_1$: Positional deviation reward: $R_1 = -|x - x_{target}| -|y - y_{target}| -|z - z_{target}|$
- $R_2$: Velocity reward: $R_2 = - |v_x| - |v_y| - |v_z|$
- $R_3$: Attitude reward: $R_3 = - |\theta| - |\phi| - |\psi|$
- $R_4$: Angular velcotiy reward: $R_4 = -|\omega_x| - |\omega_y| - |\omega_z|$
- $R_5$: Control effor reward: $R_5 = -|\Delta F_1| - |\Delta F_2| - |\Delta F_3| - |\Delta F_4|$

Here, $\alpha, \beta, \gamma, \delta, \epsilon$ are the weighting cowfficients. Their relative weighting is set such that: $\gamma > \alpha, \beta, \delta > \epsilon$
