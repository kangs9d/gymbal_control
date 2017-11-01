from main import DTracker, Video as main
import servo as srv


def movement():
  if(0 < main.p3[1] < main.original_height/2):
    if(main.original_height/2 - main.p3[1] < 10):
      pass
    elif(main.p3[1] == 0):
      pass
    else:
      srv.setAngle(0, angle++)

  else:
    if(main.p3[1] - main.original_height/2 < 10):
      pass
    else:
      srv.setAngle(0, angle++)

  if(0 < main.p3[0] < main.original_width/2):
    if(main.original_width/2 - main.p3[0] < 10):
      pass
    elif(main.p3[0] == 0):
      pass
    else:
      srv.setAngle(1, angle++)

  else:
    if(main.p3[0] - main.original_Yaw/2 < 10):
      pass
    else:
      srv.setYawDown(1, angle++)

