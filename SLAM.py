import cv2
import numpy as np

def open_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    return cap

def detect_features(image):
    detector = cv2.AKAZE_create()
    keypoints, descriptors = detector.detectAndCompute(image, None)
    return keypoints, descriptors

def match_features(descriptors1, descriptors2):
    index_params = dict(algorithm=0, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Convert descriptors to 32-bit floating-point format
    descriptors1 = descriptors1.astype(np.float32)
    descriptors2 = descriptors2.astype(np.float32)

    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    return good_matches

def estimate_pose(keypoints1, keypoints2, matches, camera_matrix):
    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    success, rotation_vec, translation_vec = cv2.solvePnP(src_pts, dst_pts, camera_matrix, None)
    return success, rotation_vec, translation_vec

def draw_tracking(frame, keypoints):
    for kp in keypoints:
        x, y = map(int, kp.pt)
        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
    return frame

def main():
    camera = open_camera()
    _, frame = camera.read()

    # You can initialize your camera matrix (intrinsics) based on your camera's properties
    focal_length = 500  # Adjust this value based on your camera
    width, height = frame.shape[1], frame.shape[0]
    camera_matrix = np.array([[focal_length, 0, width / 2], [0, focal_length, height / 2], [0, 0, 1]])

    prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_keypoints, prev_descriptors = detect_features(prev_frame)

    prev_rotation_vec = np.zeros((3, 1))
    prev_translation_vec = np.zeros((3, 1))

    while True:
        _, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        current_keypoints, current_descriptors = detect_features(gray_frame)
        matches = match_features(prev_descriptors, current_descriptors)

        print("Number of keypoints detected:", len(current_keypoints))
        print("Number of matches:", len(matches))

        # Check if we have enough matches for Essential Matrix estimation
        if len(matches) >= 8:
            src_pts = np.float32([prev_keypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([current_keypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

            # Estimate Essential Matrix and recover pose
            essential_matrix, mask = cv2.findEssentialMat(src_pts, dst_pts, camera_matrix, method=cv2.RANSAC, prob=0.999, threshold=1.0)
            _, rotation_vec, translation_vec, mask = cv2.recoverPose(essential_matrix, src_pts, dst_pts, camera_matrix)

            # Update the current camera pose with the motion estimation
            prev_rotation_vec = rotation_vec
            prev_translation_vec = translation_vec

            # Your SLAM implementation here using the pose estimation

        frame = draw_tracking(frame, current_keypoints)
        cv2.imshow('SLAM', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        prev_frame = gray_frame
        prev_keypoints = current_keypoints
        prev_descriptors = current_descriptors

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()