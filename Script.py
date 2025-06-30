import bpy

def play_mixamo_animation_sequence(armature_name, action_names_for_this_armature):
    """
    Plays a sequence of Mixamo animations on a specified armature using NLA strips.

    Args:
        armature_name (str): The name of the armature object in Blender.
        action_names_for_this_armature (list): A list of exact action names (strings)
                                               to play in sequence on THIS armature.
    """

    armature_obj = bpy.data.objects.get(armature_name)

    if not armature_obj or armature_obj.type != 'ARMATURE':
        print(f"Error: Armature object '{armature_name}' not found or is not an armature.")
        return

    # Set the armature to Pose Mode for animation control
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='POSE')

    # Ensure animation data exists for the armature
    if not armature_obj.animation_data:
        armature_obj.animation_data_create()

    # Clear existing NLA tracks on this armature to ensure clean playback
    if armature_obj.animation_data.nla_tracks:
        for track in list(armature_obj.animation_data.nla_tracks):
            armature_obj.animation_data.nla_tracks.remove(track)

    print(f"\n--- Processing Armature: '{armature_name}' ---")
    
    actions_to_play_found = []
    for name in action_names_for_this_armature:
        action = bpy.data.actions.get(name)
        if action:
            actions_to_play_found.append(action)
            print(f"Found action: '{name}' for '{armature_name}'")
        else:
            print(f"Warning: Action '{name}' not found for '{armature_name}'. Please check the name in Blender's Action Editor.")

    if not actions_to_play_found:
        print(f"No valid actions found to play for '{armature_name}'. Exiting this armature's processing.")
        return

    scene = bpy.context.scene
    
    current_strip_start_frame = 0 # Starting frame for the first NLA strip (initialized as int)

    # Add each action as an NLA strip sequentially
    for i, action in enumerate(actions_to_play_found):
        # Create a new NLA track for the action
        track = armature_obj.animation_data.nla_tracks.new()
        track.name = f"ActionTrack_{action.name}_{i}" # Unique name for the track

        # Create an NLA strip from the action
        # Convert current_strip_start_frame to int explicitly here
        strip = track.strips.new(action.name, int(current_strip_start_frame), action)
        
        # Make sure the strip plays the full action
        strip.action_frame_start = action.frame_range.x
        strip.action_frame_end = action.frame_range.y
        
        # Update the start frame for the next strip, ensuring it's an integer
        current_strip_start_frame = int(strip.frame_end) + 1 # Convert strip.frame_end to int
        
        print(f"  - Added NLA strip '{strip.name}' for action '{action.name}' from frame {strip.frame_start} to {strip.frame_end}")
    
    # Calculate the total frame range covered by the NLA strips for this armature
    min_frame = float('inf')
    max_frame = float('-inf')
    if armature_obj.animation_data.nla_tracks:
        for track in armature_obj.animation_data.nla_tracks:
            for strip in track.strips:
                min_frame = min(min_frame, strip.frame_start)
                max_frame = max(max_frame, strip.frame_end)
    else:
        min_frame = scene.frame_start
        max_frame = scene.frame_end

    # Set the scene's start/end frame to encompass the animations for this character
    scene.frame_start = min(scene.frame_start, int(min_frame))
    scene.frame_end = max(scene.frame_end, int(max_frame))
    
    # Reset to Object Mode after processing
    bpy.ops.object.mode_set(mode='OBJECT')

    print(f"Finished processing '{armature_name}'. NLA strips set up.")

# --- Call the function for each armature, with their specific actions ---

play_mixamo_animation_sequence(
    armature_name="Armature",
    action_names_for_this_armature=["Armature|mixamo.com|Layer0"]
)

play_mixamo_animation_sequence(
    armature_name="Armature.001",
    action_names_for_this_armature=["Armature.001|mixamo.com|Layer0", "Armature.001|mixamo.com|Layer0.001"]
)

bpy.context.scene.frame_current = bpy.context.scene.frame_start

print("\nAll armatures processed. Go to the Timeline editor and press Play (Spacebar) to see the animations!")