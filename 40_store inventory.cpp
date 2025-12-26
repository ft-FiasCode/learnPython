#include <iostream>
#include <string>

using namespace std;

class ProductNode {
public:
    string name;
    string brand;
    string description;
    double price;
    int quantity;
    ProductNode* next;

    ProductNode(string n, string b, string d, double p, int q) {
        name = n;
        brand = b;
        description = d;
        price = p;
        quantity = q;
        next = nullptr;
    }
};                                           

class SubCategory {
public:
    string name;
    ProductNode* head;
    int totalSold;
    int totalRemaining;

    SubCategory(string n) {
        name = n;
        head = nullptr;
        totalSold = 0;
        totalRemaining = 0;
    }

   
    void addProduct(string name, string brand, string description, double price, int quantity) {
        ProductNode* newProduct = new ProductNode(name, brand, description, price, quantity);
        newProduct->next = head;
        head = newProduct;
        totalRemaining += quantity;
        cout << "Product added to " << this->name << " sub-category." << endl;
    }

    void deleteProduct(string productName) {
        ProductNode* temp = head;
        ProductNode* prev = nullptr;

        while (temp != nullptr && temp->name != productName) {
            prev = temp;
            temp = temp->next;
        }

        if (temp == nullptr) {
            cout << "Product not found in " << this->name << " sub-category." << endl;
            return;
        }

        int quantitySold;
        cout << "Enter quantity sold (deleted) for " << productName << ": ";
        cin >> quantitySold;

        if (quantitySold > temp->quantity) {
            cout << "Cannot sell more than available quantity!" << endl;
            return;
        }

        temp->quantity -= quantitySold;
        totalSold += quantitySold;
        totalRemaining -= quantitySold;

        if (temp->quantity == 0) {

            if (prev == nullptr) {
                head = temp->next;
            } else {
                prev->next = temp->next;
            }
            cout << "Product " << productName << " deleted from " << this->name << " sub-category." << endl;
            delete temp;
        } else {
            cout << "Updated quantity of " << productName << ": " << temp->quantity << endl;
        }

        cout << "Total sold in " << this->name << ": " << totalSold << endl;
        cout << "Total remaining in " << this->name << ": " << totalRemaining << endl;
    }
    void displayProducts() {
        if (head == nullptr) {
            cout << "The sub-category " << this->name << " is empty." << endl;
            return;
        }

        ProductNode* temp = head;
        cout << "Products in " << this->name << " sub-category:" << endl;
        while (temp != nullptr) {
            cout << "Name: " << temp->name << ", Brand: " << temp->brand
                 << ", Description: " << temp->description << ", Price: $" << temp->price
                 << ", Quantity: " << temp->quantity << endl;
            temp = temp->next;
        }
    }

    void searchProduct(string productName) {
        ProductNode* temp = head;
        bool found = false;
        while (temp != nullptr) {
            if (temp->name == productName) {
                cout << "Found Product: " << endl;
                cout << "Name: " << temp->name << ", Brand: " << temp->brand
                     << ", Description: " << temp->description << ", Price: $" << temp->price
                     << ", Quantity: " << temp->quantity << endl;
                found = true;
            }
            temp = temp->next;
        }

        if (!found) {
            cout << "Product not found in " << this->name << " sub-category." << endl;
        }
    }
};

class Category {
public:
    string name;
    SubCategory* subCategories[3]; 
    int numSubCategories;

    Category(string n) {
        name = n;
        numSubCategories = 0;
    }

    void addSubCategory(string subCategoryName) {
        if (numSubCategories < 3) {
            subCategories[numSubCategories++] = new SubCategory(subCategoryName); 
        } 
        }
    void displaySubCategories() {
        cout << "Sub-categories under " << name << " category:" << endl;
        for (int i = 0; i < numSubCategories; i++) {
            cout << i + 1 << ". " << subCategories[i]->name << endl;
        }
    }

    SubCategory* selectSubCategory(int index) {
        if (index < 1 || index > numSubCategories) {
            cout << "Invalid sub-category!" << endl;
            return nullptr;
        }
        return subCategories[index - 1];
    }

    void initializeSubCategories() {
        addSubCategory("Basic Care");
        addSubCategory("Luxury Care");
        addSubCategory("Organic Care");
    }
};

class Store {
    Category* categories[4]; 
    int numCategories;

public:
    Store() {
        categories[0] = new Category("Skin Care");
        categories[1] = new Category("Jewelry");
        categories[2] = new Category("Shoes");
        categories[3] = new Category("Gadgets");
        numCategories = 4;

        for (int i = 0; i < numCategories; i++) {
            categories[i]->initializeSubCategories();
        }
    }

    void showCategories() {
        cout << "Categories: " << endl;
        for (int i = 0; i < numCategories; i++) {
            cout << i + 1 << ". " << categories[i]->name << endl;
        }
    }

    Category* selectCategory(int index) {
        if (index < 1 || index > numCategories) {
            cout << "Invalid category!" << endl;
            return nullptr;
        }
        return categories[index - 1];
    }
};

int main() {
    Store store;
    int choice, categoryIndex, subCategoryIndex;
    string productName, brand, description;
    double price;
    int quantity;

    do {
        cout << "\nMenu: \n1. Add Product\n2. Delete Product\n3. Search Product\n4. Display Products\n5. Clear Screen\n6. Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                store.showCategories();
                cout << "Select a category: ";
                cin >> categoryIndex;
                {
                    Category* selectedCategory = store.selectCategory(categoryIndex);
                    if (selectedCategory != nullptr) {
                        selectedCategory->displaySubCategories();
                        cout << "Select a sub-category: ";
                        cin >> subCategoryIndex;
                        SubCategory* selectedSubCategory = selectedCategory->selectSubCategory(subCategoryIndex);
                        if (selectedSubCategory != nullptr) {
                            cout << "Enter product name: ";
                            cin >> productName;
                            cout << "Enter brand: ";
                            cin >> brand;
                            cout << "Enter description: ";
                            cin >> description;
                            cout << "Enter price: ";
                            cin >> price;
                            cout << "Enter quantity: ";
                            cin >> quantity;
                            selectedSubCategory->addProduct(productName, brand, description, price, quantity);
                        }
                    }
                }
                break;

            case 2:
                store.showCategories();
                cout << "Select a category: ";
                cin >> categoryIndex;
                {
                    Category* selectedCategory = store.selectCategory(categoryIndex);
                    if (selectedCategory != nullptr) {
                        selectedCategory->displaySubCategories();
                        cout << "Select a sub-category: ";
                        cin >> subCategoryIndex;
                        SubCategory* selectedSubCategory = selectedCategory->selectSubCategory(subCategoryIndex);
                        if (selectedSubCategory != nullptr) {
                            cout << "Enter the name of the product to delete: ";
                            cin >> productName;
                            selectedSubCategory->deleteProduct(productName);
                        }
                    }
                }
                break;

            case 3:
                store.showCategories();
                cout << "Select a category: ";
                cin >> categoryIndex;
                {
                    Category* selectedCategory = store.selectCategory(categoryIndex);
                    if (selectedCategory != nullptr) {
                        selectedCategory->displaySubCategories();
                        cout << "Select a sub-category: ";
                        cin >> subCategoryIndex;
                        SubCategory* selectedSubCategory = selectedCategory->selectSubCategory(subCategoryIndex);
                        if (selectedSubCategory != nullptr) {
                            cout << "Enter the name of the product to search: ";
                            cin >> productName;
                            selectedSubCategory->searchProduct(productName);
                        }
                    }
                }
                break;
            case 4:
                store.showCategories();
                cout << "Select a category: ";
                cin >> categoryIndex;
                { Category* selectedCategory = store.selectCategory(categoryIndex);
                    if (selectedCategory != nullptr) {
                        selectedCategory->displaySubCategories();
                        cout << "Select a sub-category: ";
                        cin >> subCategoryIndex;
                        SubCategory* selectedSubCategory = selectedCategory->selectSubCategory(subCategoryIndex);
                        if (selectedSubCategory != nullptr) {
                            selectedSubCategory->displayProducts();
                        }
                    }
                }
                break;
            case 5:
                system("cls");
                break;

            case 6:
                cout << "Exiting..." << endl;
                break;

            default:
                cout << "Invalid choice!" << endl;
                break;
        }

    } while (choice != 6);
    return 0;
}
