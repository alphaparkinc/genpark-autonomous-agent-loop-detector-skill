from client import AgentLoopDetectorClient

def main():
    client = AgentLoopDetectorClient()
    res = client.detect_loop(history=['stepA', 'stepB', 'stepA', 'stepB'])
    print(f"Result for loop_detected: {res['loop_detected']}")

if __name__ == "__main__":
    main()
