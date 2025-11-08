from manimlib import *
import numpy as np

class DroneRLExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Reinforcement Learning for Drone Control", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # === STATE SPACE SECTION ===
        self.play(FadeOut(title))
        
        state_title = Text("State Space", font_size=42, color=BLUE)
        state_title.to_edge(UP)
        self.play(Write(state_title))
        self.wait(0.5)
        
        # State space equation with LaTeX
        state_space = Tex(
            r"[x, y, z, v_x, v_y, v_z, \theta, \phi, \psi, \omega_x, \omega_y, \omega_z, w_x, w_y, w_z]",
            font_size=32
        )
        state_space.next_to(state_title, DOWN, buff=0.8)
        self.play(Write(state_space))
        self.wait(1.5)
        
        # State space components breakdown
        position_label = Text("Position", font_size=32, color=GREEN, weight=BOLD)
        position_label.shift(UP * 1.5 + LEFT * 4)
        position_vars = Tex(r"x, y, z", font_size=28)
        position_vars.next_to(position_label, DOWN, buff=0.3)
        
        velocity_label = Text("Velocity", font_size=32, color=YELLOW, weight=BOLD)
        velocity_label.shift(UP * 1.5)
        velocity_vars = Tex(r"v_x, v_y, v_z", font_size=28)
        velocity_vars.next_to(velocity_label, DOWN, buff=0.3)
        
        attitude_label = Text("Attitude (Angles)", font_size=32, color=RED, weight=BOLD)
        attitude_label.shift(UP * 1.5 + RIGHT * 4)
        attitude_vars = Tex(r"\theta, \phi, \psi", font_size=26)
        attitude_vars.next_to(attitude_label, DOWN, buff=0.3)
        
        ang_vel_label = Text("Angular Velocity", font_size=32, color=PURPLE, weight=BOLD)
        ang_vel_label.shift(DOWN * 0.8 + LEFT * 3.5)
        ang_vel_vars = Tex(r"\omega_x, \omega_y, \omega_z", font_size=28)
        ang_vel_vars.next_to(ang_vel_label, DOWN, buff=0.3)
        
        wind_label = Text("Wind", font_size=32, color=TEAL, weight=BOLD)
        wind_label.shift(DOWN * 0.8 + RIGHT * 3.5)
        wind_vars = Tex(r"w_x, w_y, w_z", font_size=28)
        wind_vars.next_to(wind_label, DOWN, buff=0.3)
        
        self.play(FadeOut(state_space))
        self.wait(0.3)
        self.play(
            FadeIn(position_label), FadeIn(position_vars),
        )
        self.wait(0.5)
        self.play(
            FadeIn(velocity_label), FadeIn(velocity_vars),
        )
        self.wait(0.5)
        self.play(
            FadeIn(attitude_label), FadeIn(attitude_vars),
        )
        self.wait(0.5)
        self.play(
            FadeIn(ang_vel_label), FadeIn(ang_vel_vars),
        )
        self.wait(0.5)
        self.play(
            FadeIn(wind_label), FadeIn(wind_vars)
        )
        self.wait(2)
        
        # Clear state space section
        self.play(
            *[FadeOut(mob) for mob in [
                state_title, position_label, position_vars,
                velocity_label, velocity_vars, attitude_label, attitude_vars,
                ang_vel_label, ang_vel_vars, wind_label, wind_vars
            ]]
        )
        
        # === ACTION SPACE SECTION ===
        action_title = Text("Action Space", font_size=42, color=BLUE)
        action_title.to_edge(UP)
        self.play(Write(action_title))
        self.wait(0.5)
        
        # Action space with LaTeX
        action_space = Tex(
            r"[\Delta\omega_1, \Delta\omega_2, \Delta\omega_3, \Delta\omega_4]",
            font_size=36
        )
        action_space.next_to(action_title, DOWN, buff=1)
        self.play(Write(action_space))
        self.wait(1)
        
        action_desc = Text("Motor speed changes for 4 rotors", font_size=30, color=YELLOW)
        action_desc.next_to(action_space, DOWN, buff=0.8)
        self.play(FadeIn(action_desc))
        self.wait(2)
        
        # Clear action space section
        self.play(
            *[FadeOut(mob) for mob in [action_title, action_space, action_desc]]
        )
        
        # === REWARD FUNCTION SECTION ===
        reward_title = Text("Reward Function", font_size=42, color=BLUE)
        reward_title.to_edge(UP)
        self.play(Write(reward_title))
        self.wait(0.5)
        
        # Main reward equation with LaTeX
        reward_eq = Tex(
            r"R = \alpha R_1 + \beta R_2 + \gamma R_3 + \delta R_4 + \varepsilon R_5",
            font_size=38
        )
        reward_eq.next_to(reward_title, DOWN, buff=0.7)
        self.play(Write(reward_eq))
        self.wait(1.5)
        
        # Move reward equation up
        self.play(reward_eq.animate.scale(0.75).next_to(reward_title, DOWN, buff=0.4))
        
        # R1: Position reward
        r1_label = Tex(r"R_1", r"\text{: Positional deviation}", font_size=28, color=GREEN)
        r1_label.shift(UP * 1.2 + LEFT * 3)
        r1_eq = Tex(
            r"R_1 = -|x - x_{\text{target}}| - |y - y_{\text{target}}| - |z - z_{\text{target}}|",
            font_size=22
        )
        r1_eq.next_to(r1_label, DOWN, buff=0.2)
        
        # R2: Velocity reward
        r2_label = Tex(r"R_2", r"\text{: Velocity}", font_size=28, color=YELLOW)
        r2_label.next_to(r1_eq, DOWN, buff=0.4).align_to(r1_label, LEFT)
        r2_eq = Tex(r"R_2 = -|v_x| - |v_y| - |v_z|", font_size=22)
        r2_eq.next_to(r2_label, DOWN, buff=0.2)
        
        # R3: Attitude reward
        r3_label = Tex(r"R_3", r"\text{: Attitude}", font_size=28, color=RED)
        r3_label.next_to(r2_eq, DOWN, buff=0.4).align_to(r1_label, LEFT)
        r3_eq = Tex(r"R_3 = -|\theta| - |\phi| - |\psi|", font_size=22)
        r3_eq.next_to(r3_label, DOWN, buff=0.2)
        
        # R4: Angular velocity reward
        r4_label = Tex(r"R_4", r"\text{: Angular velocity}", font_size=28, color=PURPLE)
        r4_label.next_to(r3_eq, DOWN, buff=0.4).align_to(r1_label, LEFT)
        r4_eq = Tex(r"R_4 = -|\omega_x| - |\omega_y| - |\omega_z|", font_size=22)
        r4_eq.next_to(r4_label, DOWN, buff=0.2)
        
        # R5: Control effort reward
        r5_label = Tex(r"R_5", r"\text{: Control effort}", font_size=28, color=TEAL)
        r5_label.next_to(r4_eq, DOWN, buff=0.4).align_to(r1_label, LEFT)
        r5_eq = Tex(r"R_5 = -|\Delta F_1| - |\Delta F_2| - |\Delta F_3| - |\Delta F_4|", font_size=22)
        r5_eq.next_to(r5_label, DOWN, buff=0.2)
        
        # Animate reward components
        self.play(Write(r1_label), Write(r1_eq))
        self.wait(0.6)
        self.play(Write(r2_label), Write(r2_eq))
        self.wait(0.6)
        self.play(Write(r3_label), Write(r3_eq))
        self.wait(0.6)
        self.play(Write(r4_label), Write(r4_eq))
        self.wait(0.6)
        self.play(Write(r5_label), Write(r5_eq))
        self.wait(2)
        
        # Clear all rewards
        self.play(
            *[FadeOut(mob) for mob in [
                r1_label, r1_eq, r2_label, r2_eq, r3_label, r3_eq,
                r4_label, r4_eq, r5_label, r5_eq
            ]]
        )
        
        # Weight priorities
        weight_title = Text("Weight Priorities", font_size=36, color=ORANGE, weight=BOLD)
        weight_title.shift(UP * 0.8)
        self.play(Write(weight_title))
        
        # Weight hierarchy with LaTeX
        weight_hierarchy = Tex(
            r"\gamma > \alpha, \beta, \delta > \varepsilon",
            font_size=38
        )
        weight_hierarchy.next_to(weight_title, DOWN, buff=0.5)
        self.play(Write(weight_hierarchy))
        self.wait(1)
        
        weight_explanation = Text(
            "Attitude (γ) is prioritized over position/velocity/angular velocity,\n"
            "which are prioritized over control effort (ε)",
            font_size=24,
            color=GREY
        )
        weight_explanation.next_to(weight_hierarchy, DOWN, buff=0.8)
        self.play(FadeIn(weight_explanation))
        self.wait(3)
        
        # Final summary
        self.play(
            *[FadeOut(mob) for mob in [
                reward_title, reward_eq, weight_title, 
                weight_hierarchy, weight_explanation
            ]]
        )
        
        summary_title = Text("RL Drone Control Summary", font_size=44, color=BLUE, weight=BOLD)
        summary_title.to_edge(UP)
        
        summary_points = VGroup(
            Text("• 15-dimensional state space", font_size=30),
            Text("  (position, velocity, attitude, angular velocity, wind)", font_size=24, color=GREY),
            Text("", font_size=10),
            Text("• 4-dimensional action space", font_size=30),
            Text("  (motor speed changes for 4 rotors)", font_size=24, color=GREY),
            Text("", font_size=10),
            Text("• Multi-objective reward function", font_size=30),
            Text("  (balancing stability, accuracy, and efficiency)", font_size=24, color=GREY),
            Text("", font_size=10),
            Text("• Attitude prioritized for safe flight", font_size=30, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        summary_points.shift(DOWN * 0.5)
        
        self.play(Write(summary_title))
        self.wait(0.5)
        for point in summary_points:
            self.play(FadeIn(point), run_time=0.5)
        
        self.wait(3)