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

    await servo1.move(0)
    await servo2.move(0)

    await servo1.stop()
    await servo2.stop()
    
    time.sleep(3)

    errored = False

    while not errored:
        try:
            await servo1.move(180)
            await servo2.move(180)

            await servo1.stop()
            await servo2.stop()

            time.sleep(3)

            await servo1.move(0)
            await servo2.move(0)

            await servo1.stop()
            await servo2.stop()

            time.sleep(3)
        except:
            print("An exception occurred")
            errored = True
    
    await servo1.move(0)
    await servo2.move(0)

    await servo1.stop()
    await servo2.stop()

    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
