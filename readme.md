# 3D Animation Scene Setup Automation in Blender

## Project Overview

This project focuses on efficiently setting up and animating 3D character scenes in Blender. By leveraging open-source tools and Python scripting, we've established a streamlined workflow for acquiring 3D models, rigging them with ready-to-use animations, and then automating their integration and sequencing within Blender. This approach significantly reduces manual effort and speeds up animation pipeline development.

The current scene setup demonstrates the animation of **two distinct 3D characters interacting**, specifically, two models performing independent actions within the same scene, showcasing a "fighting scene" scenario.

## Workflow & Technologies Used

This project follows a clear, step-by-step methodology, integrating several powerful tools:

### 1. Blender 5.0 Alpha (Self-Built)

* **Description**: Blender is a free and open-source 3D creation suite. Its alpha versions provide access to the latest features and performance improvements before official releases. For this project, a custom build was created from the official source code.
* **Purpose**: The primary 3D environment for scene assembly, animation, and rendering.
* **Reference**: [Blender Documentation - Building Blender](https://docs.blender.org/manual/en/latest/advanced/building_blender/index.html)

### 2. FabSketch (3D Model Acquisition)

* **Description**: FabSketch (likely a typo, assuming you meant **Sketchfab** which is a popular platform) is a leading platform for sharing and discovering 3D content. It hosts a vast library of models, scenes, and animations, many of which are available under creative commons licenses.
* **Purpose**: To source high-quality 3D models and scene assets for the animation.
* **Reference**: [Sketchfab Website](https://sketchfab.com/) (Please confirm if "FabSketch" refers to a different platform, and I can update this link accordingly.)

### 3. Mixamo (Automated Rigging & Animation)

* **Description**: Mixamo is an Adobe service that provides quick, automated 3D character rigging and a vast library of motion capture animations. Users can upload a character model, let Mixamo rig it automatically, and then apply various motions.
* **Purpose**: To rapidly rig unrigged 3D models and apply pre-made, high-quality animation cycles (like walking, fighting, etc.) without manual keyframing.
* **Reference**: [Mixamo Website](https://www.mixamo.com/)

### 4. Blender Python Scripting (Animation Automation)

* **Description**: Blender's powerful Python API (`bpy`) allows for extensive automation of tasks within the software. For this project, **we collaboratively developed a custom Python script (`scripts.py`)** that significantly streamlines the animation setup process.
* **Purpose**: After downloading Mixamo-rigged models with their associated animations, manually sequencing multiple actions (e.g., a "walk" followed by a "fight") and managing them for multiple characters can be time-consuming. **The Python script was developed to automate these tasks:**
    * **Identifies specific armature objects** (your rigged characters) by name.
    * **Detects available animation actions** (the individual walk, run, fight cycles) associated with each character.
    * **Clears previous animation setups** (NLA tracks) to ensure a clean slate.
    * **Sequences multiple animation actions** for each character using Blender's Non-Linear Animation (NLA) system. This means it automatically places animation clips one after another on the timeline for each character.
    * **Manages animation for multiple independent characters simultaneously.** For instance, it can set up a "walking" animation for `Armature` and a sequence of "fighting" animations for `Armature.001` within the same scene, ensuring they play back correctly.
    * **Adjusts the overall scene timeline** to encompass the full duration of all characters' combined animation sequences.
* **Your Contribution**: The core logic for identifying armatures, clearing previous NLA setups, finding correct action names, and meticulously placing NLA strips for sequential playback on multiple distinct characters was developed and refined through our iterative discussions and problem-solving, addressing issues like incorrect action name parsing and data type errors (`float` vs `int` for frame numbers).
* **Script File**: `scripts.py` (Refer to the attached file for the full code).

## Step-by-Step Implementation

1.  **Blender Setup**:
    * Built Blender 5.0 Alpha from source code following the official Blender documentation.
    * Launched the custom-built Blender instance.

2.  **3D Model Acquisition (using FabSketch/Sketchfab)**:
    * Navigated to the FabSketch/Sketchfab website.
    * Searched and downloaded desired 3D models (e.g., character models, environmental props, scene elements).
    * Imported these models into Blender (typically via `File > Import > FBX` or `GLB/GLTF`).

3.  **Mixamo Rigging & Animation**:
    * Uploaded the unrigged 3D character models to the Mixamo website.
    * Utilized Mixamo's auto-rigger to generate an armature for each model.
    * Selected and applied various animation cycles (e.g., "walking," "fighting," "idle") from Mixamo's library to the rigged models.
    * Downloaded the rigged models with their selected animations as FBX files (ensuring "Skin" is included for the first download and "No Skin" for subsequent animation-only downloads for the same character to prevent duplicate rigs).

4.  **Blender Integration & Python Automation**:
    * Imported the Mixamo-rigged FBX models into the Blender scene. This typically resulted in armature objects named like `Armature` and `Armature.001` (for multiple characters) and their corresponding animation actions (e.g., `Armature|mixamo.com|Layer0`, `Armature.001|mixamo.com|Layer0`, `Armature.001|mixamo.com|Layer0.001`).
    * Opened Blender's **Scripting Workspace** (or `Text Editor` and `Python Console`).
    * Created a new text file (e.g., `scripts.py`) and copied the collaboratively developed Python code into it.
    * **Crucially, identified and confirmed the exact armature and animation action names within Blender's `Outliner` and `Action Editor`** (e.g., `Armature`, `Armature.001`, `Armature|mixamo.com|Layer0`, `Armature.001|mixamo.com|Layer0`, `Armature.001|mixamo.com|Layer0.001`).
    * **Modified the function calls at the end of `scripts.py`** to precisely match these names for each character and their desired animation sequence. For example:
        ```python
        # For the first character (e.g., the walker)
        play_mixamo_animation_sequence(
            armature_name="Armature",
            action_names_for_this_armature=["Armature|mixamo.com|Layer0"] # Walking action
        )

        # For the second character (e.g., the fighter)
        play_mixamo_animation_sequence(
            armature_name="Armature.001",
            action_names_for_this_armature=["Armature.001|mixamo.com|Layer0", "Armature.001|mixamo.com|Layer0.001"] # Fighting sequence
        )
        ```
    * Executed the script within Blender by clicking the "Run Script" button.
    * Verified the animation setup in the **NLA Editor** and **Timeline**, observing that NLA tracks and strips were correctly created for both `Armature` and `Armature.001`, sequencing their respective animations.
    * Pressed **Spacebar** in the Timeline to play the integrated animation scene, confirming both characters animate as intended.

## Future Enhancements

* Implementing more complex animation logic (e.g., dynamic blending between actions, state-machine driven animation).
* Developing a custom Blender UI panel for the script to allow non-technical users to select armatures and actions easily.
* Integrating external motion capture data or procedural animation techniques.

## Attached Files

* `scripts.py`: Contains the complete Python script used for automating the animation sequence setup.

**Note on Large Files:**
Due to GitHub's file size limitations, we are unable to directly upload the rendered video and the `.blend` project file to this repository. However, these assets are available through alternative methods:

* **Rendered Video (MP4/AVI/GIF)**: Available [**here**](<LINK_TO_CLOUD_STORAGE_OR_INTERNAL_SHARE>). This demonstrates the final animated output with both characters performing their sequences.
* **Blender Project File (.blend)**: Available [**here**](<LINK_TO_TO_CLOUD_STORAGE_OR_INTERNAL_SHARE>). This file contains the complete Blender scene, including the imported models, armatures, and the NLA setups generated by the script.

Please reach out to [Your Name/Team Email] if you encounter any issues accessing these files.