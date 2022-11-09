#include <iostream>
#include <src/network.h>
#include <src/transport.h>
#include <thread>
#include <cstdio>

using namespace std;

double Network::drop_probability = 0.0;
double Network::bit_flip_probability = 0.9;
size_t Network::capacity = 10 * 1024 * 1024;


int main() {
    std::cout << "*** hello" << std::endl;

    Transport t{};

    auto sender = thread([&t] {
        for (uint8_t i = 0; i<100; i++) {
            t.send(&i, 1);
        }
    });

    auto receiver = thread([&t] {
        int i = 0;
        while (i < 100) {
            uint8_t v;
            t.receive(&v, 1);
            if (v != i) {
                printf("*** expected %d, found %d\n", i, v);
                exit(0);
            }
            i++;
        }
    });

    sender.join();
    receiver.join();

    printf("*** all good\n");


    return 0;
}