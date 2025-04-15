class GravitySimulator:
    def __init__(self):
        self.bodies = []

    def add_body(self, mass, position, velocity):
        body = {
            'mass': mass,
            'position': position,
            'velocity': velocity
        }
        self.bodies.append(body)

    def update_positions(self, time_step):
        for body in self.bodies:
            body['position'][0] += body['velocity'][0] * time_step
            body['position'][1] += body['velocity'][1] * time_step

    def calculate_gravitational_force(self, body1, body2):
        G = 6.67430e-11  # gravitational constant
        dx = body2['position'][0] - body1['position'][0]
        dy = body2['position'][1] - body1['position'][1]
        distance = (dx**2 + dy**2) ** 0.5
        if distance == 0:
            return 0, 0  # avoid division by zero
        force_magnitude = G * (body1['mass'] * body2['mass']) / distance**2
        force_x = force_magnitude * (dx / distance)
        force_y = force_magnitude * (dy / distance)
        return force_x, force_y

    def update_velocities(self, time_step):
        for i, body1 in enumerate(self.bodies):
            total_force_x = 0
            total_force_y = 0
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    force_x, force_y = self.calculate_gravitational_force(body1, body2)
                    total_force_x += force_x
                    total_force_y += force_y
            body1['velocity'][0] += (total_force_x / body1['mass']) * time_step
            body1['velocity'][1] += (total_force_y / body1['mass']) * time_step