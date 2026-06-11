// Compute the expected cost of filling the FIFA world cup album just by buying packs of cars

#include <iostream>
#include <vector>
#include <ctime>

int randInt(int low, int high) {
    if (low > high) {
        return randInt(high, low);
    }
    return rand() % (high - low + 1) + low;
}

bool isComplete(std::vector<int> collection) {
    for(int i = 0; i < collection.size(); i++) {
        if(collection[i] == 0) {
            return false;
        }
    }
    return true;
}

std::vector<double> montecarloIteration(int total_cards, int cards_per_pack, int price_per_pack) {
    std::vector<int> collection(total_cards);
    double total_cost = 0;
    double packs_count = 0;
    double repeated = 0;

    while (!isComplete(collection)) {
        packs_count = packs_count + 1;
        total_cost = total_cost + price_per_pack;

        for(int i = 0; i < cards_per_pack; i++) {
            int cardIndex = randInt(1, total_cards) - 1;
            if (collection[cardIndex] > 0) {
                repeated = repeated + 1;
            }
            collection[cardIndex]++;
        }
    }

    return {packs_count, total_cost, repeated};
}

std::vector<double> montecarlo(int total_cards, int cards_per_pack, int price_per_pack, int total_iterations) {
    double average_packs_count = 0;
    double average_total_cost = 0;
    double average_repeated = 0;

    for(int i = 0; i < total_iterations; i++) {
        std::vector<double> result = montecarloIteration(total_cards, cards_per_pack, price_per_pack);
        double expected_packs_count = result[0];
        double expected_total_cost = result[1];
        double expected_repeated = result[2];

        average_packs_count = average_packs_count + expected_packs_count;
        average_total_cost = average_total_cost + expected_total_cost;
        average_repeated = average_repeated + expected_repeated;
    }

    average_packs_count = average_packs_count / total_iterations;
    average_total_cost = average_total_cost / total_iterations;
    average_repeated = average_repeated / total_iterations;

    return {average_packs_count, average_total_cost, average_repeated};
}

int main() {
    int total_cards = 980;
    int cards_per_pack = 7;
    int price_per_pack = 25;
    int montecarlo_iterations = 1000000;

    std::cout << "C++ IMPLEMENTATION\n" << std::endl; 
    std::cout << "Perfect cost to fill: " << total_cards / cards_per_pack * price_per_pack << std::endl; 
    
    srand(time(NULL)); // Seed the random number generator
    std::vector<double> result = montecarlo(total_cards, cards_per_pack, price_per_pack, montecarlo_iterations);
    double expected_packs_count = result[0];
    double expected_total_cost = result[1];
    double expected_repeated = result[2];

    std::cout << std::endl;
    std::cout << "Montecarlo results (" << montecarlo_iterations << " iterations):" << std::endl;
    std::cout << "  Expected total cost: " << expected_total_cost << std::endl;
    std::cout << "  Expected pack count: " << expected_packs_count << std::endl;
    std::cout << "  Expected repeated cards: " << expected_repeated << std::endl;

    return 0;
}