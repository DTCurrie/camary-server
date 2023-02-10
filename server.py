import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.servo import Servo

async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload='1r1riiwgnhxt0dv9scslmy05bv8xvbol96ia0rzprdsfo94z')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('camary-main.g725lybjsa.viam.cloud', opts)

async def move_to_start(servo):
    await servo.move(0)
    await asyncio.sleep(1.5)
    pos = await servo.get_position()
    print(f'move to start pos: {pos}')

async def move_to_end(servo):
    await servo.move(90)
    await asyncio.sleep(2)
    pos = await servo.get_position()
    print(f'move to end pos: {pos}')


async def main():
    robot = await connect()

    servo1 = Servo.from_robot(robot, "servo-1")
    servo2 = Servo.from_robot(robot, "servo-2")

    await move_to_start(servo1)
    await move_to_start(servo2)
    
    errored = False

    while not errored:
        try:
            await move_to_end(servo1)
            await move_to_end(servo2)

            await move_to_start(servo1)
            await move_to_start(servo2)
        except:
            print("An exception occurred")
            errored = True
    
    await move_to_start(servo1)
    await move_to_start(servo2)

    await servo1.stop()
    await servo2.stop()

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
