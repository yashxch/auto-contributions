# Learn Asynchronous Programming in Python: Introduction to `async` and `await`

# Objective:
# This tutorial introduces the fundamental concepts of asynchronous
# programming in Python using `async` and `await`. We will explore
# how to define asynchronous functions, run them concurrently, and
# understand the benefits of non-blocking operations.

import asyncio  # The core library for asynchronous I/O operations in Python.
import time     # Used to simulate work and measure execution time.

# --- Defining Asynchronous Functions ---

# The `async` keyword is used to define an asynchronous function,
# also known as a coroutine. These functions don't run immediately
# when called; instead, they return a coroutine object.
async def greet(name: str, delay: int):
    """
    An asynchronous function that simulates a greeting with a delay.

    Args:
        name: The name to greet.
        delay: The number of seconds to wait before greeting.
    """
    print(f"Starting greeting for {name}...")
    # The `await` keyword pauses the execution of the current coroutine
    # until the awaited coroutine or awaitable completes. Here, we are
    # waiting for `asyncio.sleep()` to finish. This is crucial for
    # allowing other tasks to run while this one is sleeping.
    await asyncio.sleep(delay)
    print(f"Hello, {name}! (waited {delay} seconds)")
    return f"Greeting for {name} completed."

# --- Running Asynchronous Functions Concurrently ---

# To run multiple coroutines and manage their execution, we use
# `asyncio.gather()`. This function takes multiple awaitables (like
# coroutine objects) and runs them concurrently. It returns a list
# of results once all the awaitables have completed.
async def main():
    """
    The main asynchronous function that orchestrates the concurrent
    execution of our `greet` coroutines.
    """
    print("--- Starting concurrent greetings ---")
    start_time = time.time()

    # Create coroutine objects for each greeting. Note that calling an
    # `async` function doesn't execute it; it returns a coroutine object.
    greeting_task_1 = greet("Alice", 2)
    greeting_task_2 = greet("Bob", 1)
    greeting_task_3 = greet("Charlie", 3)

    # `asyncio.gather()` schedules all the coroutine objects to run
    # concurrently. The `await` keyword here means `main` will pause
    # until all the tasks passed to `gather` are done.
    results = await asyncio.gather(
        greeting_task_1,
        greeting_task_2,
        greeting_task_3
    )

    end_time = time.time()
    print("\n--- All greetings completed ---")
    print(f"Results: {results}")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

# --- The Entry Point for Asynchronous Programs ---

# `asyncio.run()` is the entry point for running an asynchronous
# program. It takes a single coroutine (usually your `main` function)
# and handles setting up and tearing down the asyncio event loop.
# This is how you actually start the asynchronous execution.
if __name__ == "__main__":
    # This line starts the asyncio event loop, runs the `main()` coroutine,
    # and then closes the loop. It's the standard way to execute
    # top-level async code.
    asyncio.run(main())

# --- Example Usage Explanation ---
# When you run this script:
# 1. `asyncio.run(main())` starts the event loop and calls `main()`.
# 2. Inside `main()`, we create three coroutine objects: `greet("Alice", 2)`,
#    `greet("Bob", 1)`, and `greet("Charlie", 3)`.
# 3. `asyncio.gather()` takes these coroutines and schedules them to run.
# 4. The event loop starts executing them. When `greet("Alice", 2)` hits
#    `await asyncio.sleep(2)`, it pauses and yields control back to the event loop.
# 5. The event loop can then run `greet("Bob", 1)`. When `Bob` hits its sleep,
#    it also yields.
# 6. The event loop continues this process, switching between tasks whenever
#    one `await`s. This is why it's called "concurrent" or "non-blocking" –
#    tasks don't wait idly for each other; they can make progress when
#    their awaited operations are ready.
# 7. Because Bob waits for 1 second, Alice for 2, and Charlie for 3,
#    Bob will finish first, then Alice, then Charlie.
# 8. `asyncio.gather` collects their results only after all have finished.
# 9. The total execution time will be roughly the duration of the longest task (3 seconds),
#    not the sum of all delays (2+1+3 = 6 seconds), demonstrating the benefit
#    of concurrency for I/O-bound operations.