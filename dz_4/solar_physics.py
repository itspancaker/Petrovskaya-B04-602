gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star():
    type = "star"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "red"
    image = None

class Planet():
    type = "planet"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "green"
    image = None
    omega = 0.0
    #угловая скорость относительно центральной звезды (рад/с)
    sector_velocity = 0.0
    #секторная скорость


def calculate_force(body, space_objects):
    #вычисляет силу, действующую на тело со стороны всех остальных тел
    body.Fx = 0
    body.Fy = 0

    for obj in space_objects:
        if body == obj:
            continue

        dx = obj.x - body.x
        dy = obj.y - body.y

        r_squared = dx ** 2 + dy ** 2
        r = (r_squared)**0.5

        if r == 0:
            continue

        F = gravitational_constant * body.m * obj.m / r_squared

        body.Fx += F * (dx / r)
        body.Fy += F * (dy / r)


def move_space_object(body, dt, central_body=None):
    if body.m == 0:
        return

    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.Vx += ax * dt
    body.Vy += ay * dt

    body.x += body.Vx * dt
    body.y += body.Vy * dt

    #расчет угловой и секторной скорости
    if central_body and body != central_body:
        #радиус вектор от центрального тела к планете
        rx = body.x - central_body.x
        ry = body.y - central_body.y
        r_squared = rx ** 2 + ry ** 2
        r = (r_squared)**0.5

        if r > 0:
            #относительная скорость планеты
            vx_rel = body.Vx - central_body.Vx
            vy_rel = body.Vy - central_body.Vy

            #векторное произведение r x v (составляющая скорости, перпендикулярная радиус-вектору)
            p = rx * vy_rel - ry * vx_rel

            #угловая скорость omega = (r x v) / r^2
            body.omega = p / r_squared

            #секторная скорость = 0.5 * |r x v|
            body.sector_velocity = 0.5 * abs(p)


def recalculate_space_objects_positions(space_objects, dt, central_body=None):
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt, central_body)


def check_kepler_law(start_sector_vel, current_sector_vel):
    #возвращает относительную погрешность в процентах
    if start_sector_vel == 0:
        return 0.0
    error = abs(current_sector_vel - start_sector_vel) / start_sector_vel * 100
    return error


if __name__ == "__main__":
    print("This module is not for direct call!")