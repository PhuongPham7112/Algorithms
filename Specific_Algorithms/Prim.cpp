#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

struct Edge;
struct Node;
Edge* min_edge();

struct Node
{
    int numbering;
    vector<Edge*> edges = {};
    bool added = false;
};

struct Edge
{
    int start;
    int end;
    int price;
};

int main()
{
    vector<Node*> node_list;
    vector<Edge*> edge_list;
    vector<Node*> added_nodes;
    vector<Edge*> MST;

    cout << "Enter something " << endl;
    string line;
    int input;

    while (getline(cin, line)) // this is how to get a full line of cin
    {
        int city_from, city_to, price;
        stringstream ss;
        ss << line;
        ss >> city_from >> city_to >> price;

        Edge* route = new Edge;
        route->start = city_from;
        route->end = city_to;
        route->price = price;

        Node* city_1 = new Node;
        city_1->numbering = city_from;
        city_1->edges.push_back(route);

        Node* city_2 = new Node;
        city_2->numbering = city_to;
        city_2->edges.push_back(route);

        node_list.push_back(city_1);
        node_list.push_back(city_2);
        edge_list.push_back(route);
    };

    // start the logic
    while (added_nodes.size() != node_list.size()) // while not all nodes are included in MST
    {
        Node* chosen_node = node_list.back(); // choose a starting node
        int min = 0;
        Edge* min_edge;
        for (Edge* e: chosen_node->edges)
        {
            if (e->price < min)
            {
                min_edge = e;
            };
        };
        MST.push_back(min_edge);
        
    }

    // ending
    for (Node* i: node_list)
    {
        cout << "delete node" << endl;
        cout << i->numbering << endl;
        delete i;
    };

    for (Edge* x: edge_list)
    {
        cout << "delete edge" << endl;
        cout << x->price << endl;
        delete x;
    };

    cout << "Ending..." << endl;

    return 0;
};

