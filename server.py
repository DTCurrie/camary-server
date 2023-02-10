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

async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)

    servo1 = Servo.from_robot(robot, "servo-1")
    servo2 = Servo.from_robot(robot, "servo-2")

    s1Pos = await servo1.get_position()
    s2Pos = await servo2.get_position()

    print(f'Servo 1 Position: {s1Pos}')
    print(f'Servo 2 Position: {s2Pos}')

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
