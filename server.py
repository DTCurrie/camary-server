import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.servo import Servo

degs = [0, 15, 30, 45, 60, 75, 90]

async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload='1r1riiwgnhxt0dv9scslmy05bv8xvbol96ia0rzprdsfo94z')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('camary-main.g725lybjsa.viam.cloud', opts)

async def move_to_deg(servo, deg):
    await servo.move(deg)
    await asyncio.sleep(5)
    pos = await servo.get_position()

async def main():
    robot = await connect()

    servo1 = Servo.from_robot(robot, "servo-1")
    servo2 = Servo.from_robot(robot, "servo-2")

    await move_to_deg(servo1, 0)
    await move_to_deg(servo2, 0)
    
    errored = False

    while not errored:
        try:
            for deg in degs:
                await move_to_deg(servo1, deg)
                await move_to_deg(servo2, deg)
        except:
            print("An exception occurred")
            errored = True
    
    await move_to_deg(servo1, 0)
    await move_to_deg(servo2, 0)

    await servo1.stop()
    await servo2.stop()

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
