import gfootball.env as football_env
import os
import json

def record_game_video(
    env_name='academy_empty_goal_close',
    representation='simple115v2',
    logdir='./videos',
    num_episodes=3,
    max_steps=500,
    save_obs=False
):
    """Record a video of football games using Google Research Football."""
    print(f"Creating environment '{env_name}' with video recording enabled...")

    env = football_env.create_environment(
        env_name=env_name,
        representation=representation,
        render=True,
        write_video=True,
        write_full_episode_dumps=True,
        logdir=logdir,
        dump_frequency=1
    )

    for episode in range(num_episodes):
        print(f"\n--- Recording episode {episode + 1}/{num_episodes} ---")
        obs = env.reset()
        done = False
        step_count = 0
        episode_obs = []

        while not done and step_count < max_steps:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            step_count += 1

            if save_obs:
                episode_obs.append(obs)

            if step_count % 100 == 0:
                print(f"  Step {step_count}: reward = {reward}")

        print(f"Episode finished after {step_count} steps.")

        if save_obs:
            obs_file = os.path.join(logdir, f"episode_{episode+1}_obs.json")
            with open(obs_file, 'w') as f:
                json.dump(episode_obs, f, indent=2, default=str)
            print(f"  Observations saved to: {obs_file}")

        if 'dumps' in info:
            for dump_info in info['dumps']:
                if 'video' in dump_info:
                    print(f"  Video saved: {dump_info['video']}")

    env.close()
    print("\nAll recordings completed. Check the './videos' directory for output files.")

if __name__ == "__main__":
    record_game_video()
