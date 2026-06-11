// Compute the expected cost of filling the FIFA world cup album just by buying packs of cars

#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "string.h"

#define bool char
#define false 0
#define true 1

int randInt(int low, int high) {
    if (low > high) {
        int temp = low;
        low = high;
        high = temp;
    }
    return rand() % (high - low + 1) + low;
}

void clearCollection(int* collection, int size) {
    memset(collection, 0, size * sizeof(int));
}

void montecarloIteration(int total_cards, int cards_per_pack, int price_per_pack, int* collection, double *result) {
    double total_cost = 0;
    double packs_count = 0;
    double repeated = 0;
    int unique_cards = 0;

    clearCollection(collection, total_cards);

    while (unique_cards < total_cards) {
        packs_count = packs_count + 1;
        total_cost = total_cost + price_per_pack;

        for(int i = 0; i < cards_per_pack; i++) {
            int cardIndex = randInt(1, total_cards) - 1;
            if (collection[cardIndex] == 0) {
                unique_cards++;
            } else {
                repeated = repeated + 1;
            }
            collection[cardIndex]++;
        }
    }

    result[0] = packs_count;
    result[1] = total_cost;
    result[2] = repeated;

    return;
}

void montecarlo(int total_cards, int cards_per_pack, int price_per_pack, int total_iterations, double* result) {
    double average_packs_count = 0;
    double average_total_cost = 0;
    double average_repeated = 0;

    double* iteration_result = malloc(3 * sizeof(double));
    int* collection = malloc(total_cards * sizeof(int));

    double expected_packs_count = 0;
    double expected_total_cost = 0;
    double expected_repeated = 0;
    for(int i = 0; i < total_iterations; i++) {
        montecarloIteration(total_cards, cards_per_pack, price_per_pack, collection, iteration_result);
        expected_packs_count = iteration_result[0];
        expected_total_cost = iteration_result[1];
        expected_repeated = iteration_result[2];

        average_packs_count = average_packs_count + expected_packs_count;
        average_total_cost = average_total_cost + expected_total_cost;
        average_repeated = average_repeated + expected_repeated;
    }

    average_packs_count = average_packs_count / total_iterations;
    average_total_cost = average_total_cost / total_iterations;
    average_repeated = average_repeated / total_iterations;

    result[0] = average_packs_count;
    result[1] = average_total_cost;
    result[2] = average_repeated;

    free(iteration_result);
    free(collection);

    return;
}

int main() {
    int total_cards = 980;
    int cards_per_pack = 7;
    int price_per_pack = 25;
    int montecarlo_iterations = 1000000;

    double perfect_cost = total_cards / cards_per_pack * price_per_pack;
    printf("C IMPLEMENTATION\n\n");
    printf("Perfect cost to fill: %.2f\n\n", perfect_cost);

    srand(time(0));
    double* result = malloc(3 * sizeof(double));

    montecarlo(total_cards, cards_per_pack, price_per_pack, montecarlo_iterations, result);
    double expected_packs_count = result[0];
    double expected_total_cost = result[1];
    double expected_repeated = result[2];
    printf("Montecarlo results (%d iterations):\n", montecarlo_iterations);
    printf("  Expected total cost: %.2f\n", expected_total_cost);
    printf("  Expected pack count: %.2f\n", expected_packs_count);
    printf("  Expected repeated cards: %.2f\n", expected_repeated);

    free(result);

    return 0;
}