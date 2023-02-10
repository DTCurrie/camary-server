import asyncio
import time

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

    servo1 = Servo.from_robot(robot, "servo-1")
    servo2 = Servo.from_robot(robot, "servo-2")

    print('move to 0')

    await servo1.move(0)
    await servo2.move(0)

    time.sleep(5)

    print('move to 10')

    await servo1.move(10)
    await servo2.move(10)

    time.sleep(5)

    print('move to 20')

    await servo1.move(20)
    await servo2.move(20)

    time.sleep(5)

    print('move to 30')

    await servo1.move(30)
    await servo2.move(30)

    time.sleep(5)

    print('move to 40')

    await servo1.move(40)
    await servo2.move(40)

    time.sleep(5)

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
