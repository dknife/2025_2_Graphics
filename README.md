# 2025_2 3D 그래픽스 프로그래밍 (게임공학과 전공교과)

동명대학교 게임학부 강영민 교수

수업의 목표
* 컴퓨터 그래픽의 기본 개념을 이해한다.
* 실시간 그래픽스와 오프라인 그래픽스의 차이를 이해하고 게임개발에 적용한다.
* OpenGL 및 DirectX를 이용하여 실시간 그래픽스 콘텐츠를 구현할 수 있는 기초 역량을 갖춘다.

수업의 내용
* 컴퓨터 게임과 같이 가상 환경을 다루는 애플리케이션들은 컴퓨터 그래픽스라는 기술적 바탕 위에서 구현된다. 본 교과목은 이러한 기술적 바탕이 되는 그래픽스 이론에 대한 이해와 함께 이를 실제로 구현하는 다양한 기술들을 이해하고 활용할 수 있도록 한다.

강의 자료: 홈페이지 공개 자료 및 유인물

## 사용환경

* 프로그래밍 언어: Python
* 핵심 패키지: PyOpenGL, glfw
```
% pip install PyOpenGL glfw
```

## 과제

### 과제 1
집에 있는 컴퓨터나 가지고 있는 노트북에 파이썬 환경을 설치하고 그래픽스 수업에 필요한 패키지 (PyOpenGL, Numpy 등)을 설치한 뒤 삼각형을 그려본다.

## Lec 0: 그래픽스 소개

[그래픽스 소개](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec01_Introduction2Graphics.pdf)

## Lec 1: OpenGL 소개

[OpenGL 소개](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec02_BasicGraphicsProgramming_Pres.pdf)

* [파이썬 간단 소개](https://colab.research.google.com/drive/1gHI_fN4RDK4pkVe7TSN2-zFjrMBC-dR5?usp=sharing)

* [실습1](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec01/01_glfwWindow.py)

## Lec 2: Primitive의 이해

[OpenGL 프로그래밍의 시작](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec03_Primitives_Pres.pdf)

* [실습 1 간단한 그래픽 윈도우의 생성](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec02/0201_GLWindow.py)

* [실습 2 오픈지엘 기본 코드](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec02/0202_GLCoding.py)

* [실습 3 프리미티브 연습](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec02/0203_Drawing.py)

* [프로젝트 １ 마우스를 이용한 정점 입력](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec02/project1_mouse.py)

* [프로젝트 ２ 마우스와 키보드를 이용한 정점／프리미티브 입력](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec02/project2_mouse_key.py)

## Lec 3: 카메라 투영의 이해

[카메라 투영](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec04_CameraProjection_pres.pdf)

* [공동 코드 myglfw.py](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/myglfw.py)

* [실습 1 공동 코드를 활용한 간단한 그리기](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/0301_camera.py)

* [실습 2 종횡비를 이용한 glOrtho 설정](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/0302_glOrtho_noDistort.py)

* [실습 3 두 개의 뷰포트 생성](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/0303_twoViewport.py)

* [실습 4 glOrtho 관측공간 제어](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/0304_glOrthoVisualize.py)

* [실습 5 glFrustum 관측공간 제어](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec03/0305_frustumVisualize.py)

## Lec 4: 렌더링 속도 개선

[디스플레이 리스트와 정점 버퍼](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec05_RenderingEfficiency_pres.pdf)

* [개선된 공동 코드 myglfw.py](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/myglfw.py)

* [실습 1 카메라와 평면 그려보기](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/0401_camera_00.py)

* [실습 2 키보드를 이용하여 카메라 움직여 보기](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/0402_camera_move.py)

* [실습 3 디스플레이 리스트로 렌더링 속도 개선](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/0403_complexPlane.py)

* [실습 4 버텍스 버퍼를 이용한 렌더링 속도 개선](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/0404_vertexBuffer.py)

* [실습 5 렌더링 기법 비교](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec04/0406_comparison.py)


## Lec 5: 메시 읽기

[메시 읽기](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec06_MeshLoading_pres.pdf)

#### 실습

* [가장 기본적인 메시 읽기 테스트](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code05)
* [실습 기본 코드](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Lec05)
* [빠른 면 그리기가 가능한 버전 1 - DisplayList](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code06)
* [빠른 면 그리기가 가능한 버전 2 - DrawArrays DrawElements](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code06_drawElements)

  
[데이터]

* [메시 데이터 예시](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/mesh.txt)
* [소 메시 데이터](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/cow.txt)
* [두개골 메시](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/skull.txt)

## Lec 6: 계층적 모델링

[계층적 모델링](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec07_HierarchicalModeling_pres.pdf)

#### 실습

* [변환 기본 코드](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code07_transform)

* [로봇 기본 코드](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code07_robot)

* [태양계 기본 코드](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code07_solarSystem)

## Lec 7: 색과 조명

[색과 조명](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec08_Colors_Lights_pres.pdf)

#### 실습

* [색상의 지정](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Code08_Color/01ColorTest.py)

* [조명 설정](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Code08_Color/02LightModel.py)
  
* [메시에 재질 설정하고 조명 비추기](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code08_Color)

## Lec 8: 텍스처 매핑

[텍스처 매핑 - 다중텍스처, 자동텍스처 좌표](https://github.com/dknife/2025_2_Graphics/raw/main/LectureNotes/Lec10_TextureMapping.pdf)

* [실습 1 기본코드](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code10_Texture_A)

* [실습 2 랜덤 이미지 사용](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code10_Texture_B)

* [실습 3 이미지 파일 로딩하여 사용하기](https://github.com/dknife/2025_2_Graphics/tree/main/Code/Code10_Texture_C)
  
  * [이미지 파일 데이터](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec10_Texture/photo.jpg)
  * [이미지 파일 데이터](https://github.com/dknife/2025_2_Graphics/blob/main/Code/Lec10_Texture/photo2.png)

